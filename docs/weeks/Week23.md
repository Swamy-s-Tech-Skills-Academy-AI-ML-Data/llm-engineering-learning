# Week 23: Frontend Integration (React, Angular, Next.js)

**Theme:** Frontend LLM Integration  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** LLM-powered frontend applications in React, Angular, and Next.js  
**Platforms:** OpenAI + Azure OpenAI (React, Angular, Next.js mastery)

---

## 🎯 Week 23 Learning Objectives

By the end of this week, you will:
- [ ] Integrate LLMs into React applications
- [ ] Build Angular services for LLM integration
- [ ] Create Next.js applications with LLM APIs
- [ ] Implement real-time streaming UI
- [ ] Handle loading states and errors
- [ ] Build responsive LLM UIs

---

## 📅 Day-by-Day Breakdown

### Day 1: React Integration (30 minutes)

**Learning Goal:** Integrate OpenAI and Azure OpenAI into React

**Tasks (30 min):**

1. **React Setup** (10 min)
   ```bash
   npx create-react-app llm-react-app
   cd llm-react-app
   npm install openai axios
   ```

2. **React Hooks for LLM** (20 min)
   ```javascript
   // useLLM.js hook
   import { useState, useCallback } from 'react';
   import OpenAI from 'openai';
   
   const useLLM = (provider = 'openai') => {
       const [loading, setLoading] = useState(false);
       const [error, setError] = useState(null);
       const [response, setResponse] = useState('');
       
       const client = provider === 'openai' 
           ? new OpenAI({ apiKey: process.env.REACT_APP_OPENAI_API_KEY })
           : new AzureOpenAI({
               apiKey: process.env.REACT_APP_AZURE_OPENAI_API_KEY,
               endpoint: process.env.REACT_APP_AZURE_OPENAI_ENDPOINT,
               apiVersion: '2024-02-15-preview'
           });
       
       const sendMessage = useCallback(async (messages, model = 'gpt-3.5-turbo') => {
           setLoading(true);
           setError(null);
           
           try {
               const completion = await client.chat.completions.create({
                   model: model,
                   messages: messages,
               });
               
               setResponse(completion.choices[0].message.content);
               return completion.choices[0].message.content;
           } catch (err) {
               setError(err.message);
               throw err;
           } finally {
               setLoading(false);
           }
       }, [provider]);
       
       return { sendMessage, loading, error, response };
   };
   
   // Usage in component
   function ChatComponent() {
       const { sendMessage, loading, error, response } = useLLM('azure_openai');
       const [messages, setMessages] = useState([]);
       
       const handleSend = async (userMessage) => {
           const newMessages = [...messages, { role: 'user', content: userMessage }];
           setMessages(newMessages);
           
           const aiResponse = await sendMessage(newMessages);
           setMessages([...newMessages, { role: 'assistant', content: aiResponse }]);
       };
       
       return (
           <div>
               {loading && <div>Loading...</div>}
               {error && <div>Error: {error}</div>}
               <div>{response}</div>
               <button onClick={() => handleSend('Hello!')}>Send</button>
           </div>
       );
   }
   ```

**Exercise:**
- [ ] Create React app with LLM integration
- [ ] Implement useLLM hook
- [ ] Build chat interface

---

### Day 2: Angular Integration (30 minutes)

**Learning Goal:** Integrate OpenAI and Azure OpenAI into Angular

**Tasks (30 min):**

1. **Angular Setup** (10 min)
   ```bash
   ng new llm-angular-app
   cd llm-angular-app
   npm install openai
   ```

2. **Angular Service for LLM** (20 min)
   ```typescript
   // llm.service.ts
   import { Injectable } from '@angular/core';
   import { HttpClient } from '@angular/common/http';
   import { Observable } from 'rxjs';
   
   @Injectable({
       providedIn: 'root'
   })
   export class LLMService {
       private apiUrl = '/api/llm'; // Backend proxy
       
       constructor(private http: HttpClient) {}
       
       chatCompletion(
           messages: Array<{role: string, content: string}>,
           model: string = 'gpt-3.5-turbo',
           provider: 'openai' | 'azure_openai' = 'openai'
       ): Observable<any> {
           return this.http.post(this.apiUrl, {
               provider,
               model,
               messages
           });
       }
   }
   
   // component.ts
   import { Component } from '@angular/core';
   import { LLMService } from './llm.service';
   
   @Component({
       selector: 'app-chat',
       template: `
           <div *ngIf="loading">Loading...</div>
           <div *ngIf="error">{{ error }}</div>
           <div *ngFor="let message of messages">
               <p>{{ message.content }}</p>
           </div>
           <button (click)="sendMessage()">Send</button>
       `
   })
   export class ChatComponent {
       messages: Array<{role: string, content: string}> = [];
       loading = false;
       error: string | null = null;
       
       constructor(private llmService: LLMService) {}
       
       sendMessage() {
           this.loading = true;
           this.llmService.chatCompletion(
               this.messages,
               'gpt-4',
               'azure_openai'
           ).subscribe({
               next: (response) => {
                   this.messages.push({
                       role: 'assistant',
                       content: response.content
                   });
                   this.loading = false;
               },
               error: (err) => {
                   this.error = err.message;
                   this.loading = false;
               }
           });
       }
   }
   ```

**Exercise:**
- [ ] Create Angular service
- [ ] Build Angular component
- [ ] Implement error handling

---

### Day 3: Next.js Integration (30 minutes)

**Learning Goal:** Integrate OpenAI and Azure OpenAI into Next.js

**Tasks (30 min):**

1. **Next.js Setup** (10 min)
   ```bash
   npx create-next-app@latest llm-nextjs-app
   cd llm-nextjs-app
   npm install openai
   ```

2. **Next.js API Routes + Frontend** (20 min)
   ```typescript
   // pages/api/chat.ts (API route)
   import type { NextApiRequest, NextApiResponse } from 'next';
   import OpenAI from 'openai';
   import { AzureOpenAI } from 'openai';
   
   export default async function handler(
       req: NextApiRequest,
       res: NextApiResponse
   ) {
       if (req.method !== 'POST') {
           return res.status(405).json({ error: 'Method not allowed' });
       }
       
       const { provider, model, messages } = req.body;
       
       const client = provider === 'openai'
           ? new OpenAI({ apiKey: process.env.OPENAI_API_KEY })
           : new AzureOpenAI({
               apiKey: process.env.AZURE_OPENAI_API_KEY!,
               endpoint: process.env.AZURE_OPENAI_ENDPOINT!,
               apiVersion: '2024-02-15-preview'
           });
       
       try {
           const completion = await client.chat.completions.create({
               model: model,
               messages: messages,
           });
           
           return res.status(200).json({
               content: completion.choices[0].message.content
           });
       } catch (error: any) {
           return res.status(500).json({ error: error.message });
       }
   }
   
   // pages/index.tsx (Frontend)
   import { useState } from 'react';
   
   export default function Home() {
       const [messages, setMessages] = useState([]);
       const [loading, setLoading] = useState(false);
       
       const sendMessage = async (content: string) => {
           setLoading(true);
           
           const response = await fetch('/api/chat', {
               method: 'POST',
               headers: { 'Content-Type': 'application/json' },
               body: JSON.stringify({
                   provider: 'azure_openai',
                   model: 'gpt-4',
                   messages: [...messages, { role: 'user', content }]
               })
           });
           
           const data = await response.json();
           setMessages([...messages, 
               { role: 'user', content },
               { role: 'assistant', content: data.content }
           ]);
           setLoading(false);
       };
       
       return (
           <div>
               {/* Chat UI */}
           </div>
       );
   }
   ```

**Exercise:**
- [ ] Create Next.js API route
- [ ] Build frontend component
- [ ] Test end-to-end flow

---

### Day 4: Streaming & Real-Time Updates (30 minutes)

**Learning Goal:** Implement streaming responses in frontend

**Tasks (30 min):**

1. **Streaming Implementation** (20 min)
   ```javascript
   // React streaming example
   const useStreamingLLM = () => {
       const [streamingText, setStreamingText] = useState('');
       
       const streamMessage = async (messages) => {
           const response = await fetch('/api/chat/stream', {
               method: 'POST',
               body: JSON.stringify({ messages })
           });
           
           const reader = response.body.getReader();
           const decoder = new TextDecoder();
           
           while (true) {
               const { done, value } = await reader.read();
               if (done) break;
               
               const chunk = decoder.decode(value);
               const lines = chunk.split('\n');
               
               for (const line of lines) {
                   if (line.startsWith('data: ')) {
                       const data = JSON.parse(line.slice(6));
                       setStreamingText(prev => prev + data.content);
                   }
               }
           }
       };
       
       return { streamMessage, streamingText };
   };
   ```

2. **Optimistic UI Updates** (10 min)
   - Loading states
   - Error boundaries
   - Retry logic

**Exercise:**
- [ ] Implement streaming
- [ ] Add loading states
- [ ] Handle errors gracefully

---

### Day 5: Review & Practice (30 minutes)

**Tasks:**
- Review frontend patterns
- Complete exercises
- Week 23 reflection

**Deliverable:**
- [ ] React app with LLM
- [ ] Angular app with LLM
- [ ] Next.js app with LLM
- [ ] Streaming implementation

---

## 🔄 Next Week Preview

**Week 24:** .NET Ecosystem (Aspire, Web API, Blazor)
- .NET Aspire orchestration
- .NET Web API backend
- Blazor frontend
- Azure OpenAI integration
- Full-stack .NET LLM applications

