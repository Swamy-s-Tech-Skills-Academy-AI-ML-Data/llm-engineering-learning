# Week 24: .NET Ecosystem (Aspire, Web API, Blazor)

**Theme:** .NET LLM Integration  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Full-stack .NET LLM applications with Aspire, Web API, and Blazor  
**Platforms:** OpenAI + Azure OpenAI (Aspire, Web API, Blazor mastery)

---

## 🎯 Week 24 Learning Objectives

By the end of this week, you will:
- [ ] Build .NET Aspire orchestrated applications
- [ ] Create .NET Web API backends for LLM integration
- [ ] Develop Blazor frontends with LLM features
- [ ] Integrate OpenAI and Azure OpenAI in .NET
- [ ] Implement dependency injection patterns
- [ ] Build production-ready .NET LLM applications

---

## 📅 Day-by-Day Breakdown

### Day 1: .NET Web API with OpenAI & Azure OpenAI (30 minutes)

**Learning Goal:** Build .NET Web API backend for LLM integration

**Tasks (30 min):**

1. **Project Setup** (10 min)
   ```bash
   dotnet new webapi -n LLM.Api
   cd LLM.Api
   dotnet add package Azure.AI.OpenAI
   dotnet add package OpenAI
   ```

2. **Service Implementation** (20 min)
   ```csharp
   // Services/ILLMService.cs
   public interface ILLMService
   {
       Task<string> GetChatCompletionAsync(
           List<ChatMessage> messages, 
           string model, 
           CancellationToken cancellationToken = default);
   }
   
   // Services/OpenAIService.cs
   public class OpenAIService : ILLMService
   {
       private readonly OpenAI.OpenAIClient _client;
       private readonly ILogger<OpenAIService> _logger;
       
       public OpenAIService(IConfiguration configuration, ILogger<OpenAIService> logger)
       {
           var apiKey = configuration["OpenAI:ApiKey"];
           _client = new OpenAI.OpenAIClient(apiKey);
           _logger = logger;
       }
       
       public async Task<string> GetChatCompletionAsync(
           List<ChatMessage> messages, 
           string model, 
           CancellationToken cancellationToken = default)
       {
           var request = new ChatCompletionRequest
           {
               Messages = messages.Select(m => new ChatMessage
               {
                   Role = m.Role,
                   Content = m.Content
               }).ToList(),
               Model = model,
               Temperature = 0.7f
           };
           
           var response = await _client.GetChatCompletionsAsync(
               model, 
               request, 
               cancellationToken);
           
           return response.Value.Choices[0].Message.Content;
       }
   }
   
   // Services/AzureOpenAIService.cs
   public class AzureOpenAIService : ILLMService
   {
       private readonly AzureOpenAIClient _client;
       private readonly ILogger<AzureOpenAIService> _logger;
       
       public AzureOpenAIService(IConfiguration configuration, ILogger<AzureOpenAIService> logger)
       {
           var endpoint = configuration["AzureOpenAI:Endpoint"];
           var apiKey = configuration["AzureOpenAI:ApiKey"];
           var credential = new AzureKeyCredential(apiKey);
           _client = new AzureOpenAIClient(new Uri(endpoint), credential);
           _logger = logger;
       }
       
       public async Task<string> GetChatCompletionAsync(
           List<ChatMessage> messages, 
           string deploymentName, 
           CancellationToken cancellationToken = default)
       {
           var chatCompletionsOptions = new ChatCompletionsOptions
           {
               DeploymentName = deploymentName,
               Messages = messages.Select(m => new ChatRequestUserMessage(m.Content)).ToList(),
               Temperature = 0.7f
           };
           
           var response = await _client.GetChatCompletionsAsync(
               chatCompletionsOptions, 
               cancellationToken);
           
           return response.Value.Choices[0].Message.Content;
       }
   }
   
   // Controllers/ChatController.cs
   [ApiController]
   [Route("api/[controller]")]
   public class ChatController : ControllerBase
   {
       private readonly ILLMService _llmService;
       
       public ChatController(ILLMService llmService)
       {
           _llmService = llmService;
       }
       
       [HttpPost]
       public async Task<IActionResult> Chat([FromBody] ChatRequest request)
       {
           try
           {
               var response = await _llmService.GetChatCompletionAsync(
                   request.Messages, 
                   request.Model);
               
               return Ok(new { content = response });
           }
           catch (Exception ex)
           {
               return StatusCode(500, new { error = ex.Message });
           }
       }
   }
   
   // Program.cs - Dependency Injection
   var builder = WebApplication.CreateBuilder(args);
   
   // Register LLM service based on configuration
   var provider = builder.Configuration["LLM:Provider"];
   if (provider == "openai")
   {
       builder.Services.AddScoped<ILLMService, OpenAIService>();
   }
   else if (provider == "azure_openai")
   {
       builder.Services.AddScoped<ILLMService, AzureOpenAIService>();
   }
   
   var app = builder.Build();
   app.MapControllers();
   app.Run();
   ```

**Exercise:**
- [ ] Create .NET Web API project
- [ ] Implement both OpenAI and Azure OpenAI services
- [ ] Test API endpoints

---

### Day 2: .NET Aspire Orchestration (30 minutes)

**Learning Goal:** Orchestrate LLM services with .NET Aspire

**Tasks (30 min):**

1. **Aspire Setup** (10 min)
   ```bash
   dotnet new aspire-starter -n LLM.Aspire
   cd LLM.Aspire
   ```

2. **Aspire Orchestration** (20 min)
   ```csharp
   // AppHost/Program.cs
   var builder = DistributedApplication.CreateBuilder(args);
   
   // Add API project
   var apiService = builder.AddProject<Projects.LLM_Api>("llm-api")
       .WithReference(redis)
       .WithEnvironment("LLM__Provider", "azure_openai");
   
   // Add Blazor frontend
   var blazorApp = builder.AddProject<Projects.LLM_Blazor>("llm-blazor")
       .WithReference(apiService);
   
   // Add Redis for caching
   var redis = builder.AddRedis("redis");
   
   // Add Azure OpenAI connection
   var azureOpenAI = builder.AddConnectionString("AzureOpenAI");
   
   builder.Build().Run();
   ```

**Exercise:**
- [ ] Set up Aspire project
- [ ] Configure services
- [ ] Test orchestration

---

### Day 3: Blazor Frontend (30 minutes)

**Learning Goal:** Build Blazor frontend with LLM integration

**Tasks (30 min):**

1. **Blazor Setup** (10 min)
   ```bash
   dotnet new blazor -n LLM.Blazor
   cd LLM.Blazor
   ```

2. **Blazor Components** (20 min)
   ```razor
   @* Pages/Chat.razor *@
   @page "/chat"
   @inject ILLMApiService LLMService
   @inject ILogger<Chat> Logger
   
   <PageTitle>LLM Chat</PageTitle>
   
   <h3>Chat with LLM</h3>
   
   <div class="chat-container">
       <div class="messages">
           @foreach (var message in messages)
           {
               <div class="message @message.Role">
                   <strong>@message.Role:</strong> @message.Content
               </div>
           }
       </div>
       
       @if (loading)
       {
           <div class="loading">Loading...</div>
       }
       
       <div class="input-area">
           <input @bind="userInput" @bind:event="oninput" 
                  placeholder="Type your message..." />
           <button @onclick="SendMessage" disabled="@loading">Send</button>
           <select @bind="selectedProvider">
               <option value="openai">OpenAI</option>
               <option value="azure_openai">Azure OpenAI</option>
           </select>
       </div>
   </div>
   
   @code {
       private List<ChatMessage> messages = new();
       private string userInput = string.Empty;
       private bool loading = false;
       private string selectedProvider = "azure_openai";
       
       private async Task SendMessage()
       {
           if (string.IsNullOrWhiteSpace(userInput)) return;
           
           messages.Add(new ChatMessage { Role = "user", Content = userInput });
           var userMessage = userInput;
           userInput = string.Empty;
           loading = true;
           
           try
           {
               var response = await LLMService.GetChatCompletionAsync(
                   messages, 
                   "gpt-4", 
                   selectedProvider);
               
               messages.Add(new ChatMessage 
               { 
                   Role = "assistant", 
                   Content = response 
               });
           }
           catch (Exception ex)
           {
               Logger.LogError(ex, "Error sending message");
               // Handle error
           }
           finally
           {
               loading = false;
           }
       }
   }
   
   // Services/ILLMApiService.cs
   public interface ILLMApiService
   {
       Task<string> GetChatCompletionAsync(
           List<ChatMessage> messages, 
           string model, 
           string provider);
   }
   
   // Services/LLMApiService.cs
   public class LLMApiService : ILLMApiService
   {
       private readonly HttpClient _httpClient;
       
       public LLMApiService(HttpClient httpClient)
       {
           _httpClient = httpClient;
       }
       
       public async Task<string> GetChatCompletionAsync(
           List<ChatMessage> messages, 
           string model, 
           string provider)
       {
           var request = new
           {
               messages = messages,
               model = model,
               provider = provider
           };
           
           var response = await _httpClient.PostAsJsonAsync("/api/chat", request);
           response.EnsureSuccessStatusCode();
           
           var result = await response.Content.ReadFromJsonAsync<ChatResponse>();
           return result.Content;
       }
   }
   ```

**Exercise:**
- [ ] Create Blazor app
- [ ] Implement chat component
- [ ] Connect to API

---

### Day 4: Full-Stack Integration (30 minutes)

**Learning Goal:** Integrate all .NET components

**Tasks (30 min):**

1. **Complete Integration** (20 min)
   - Connect Blazor to Web API
   - Configure Aspire orchestration
   - Add error handling
   - Implement logging

2. **Testing** (10 min)
   - Test end-to-end flow
   - Verify both providers work
   - Check performance

**Exercise:**
- [ ] Complete full integration
- [ ] Test with OpenAI
   - Test with Azure OpenAI
   - Document setup process

---

### Day 5: Review & Practice (30 minutes)

**Tasks:**
- Review .NET patterns
- Complete exercises
- Week 24 reflection

**Deliverable:**
- [ ] Working .NET Web API
- [ ] Aspire orchestration
- [ ] Blazor frontend
- [ ] Full-stack application

---

## 🔄 Next Week Preview

**Week 25:** Agentic Frameworks Mastery
- LangChain implementation
- LangGraph workflows
- OpenAI Agent SDK
- Azure Agent SDK
- Framework comparison and selection

