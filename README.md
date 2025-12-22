# Knit.dev
Knit.dev is an AI-powered coding agent that intelligently orchestrates a team of specialized AI agents to build, debug, and manage entire software projects from a single prompt, all within your terminal.

## First Prototype Architecture

```mermaid
flowchart TD
    U[User Prompt]

    subgraph TL[Tech Lead Agent]
        P[Analyze Prompt & Plan Requirements]
        Q{Clarification Needed?}
        A[Ask User Questions]
    end

    subgraph FE[Frontend Subagent]
        FE1[Design UI & UX]
        FE2[Implement Frontend Code]
    end

    subgraph BE[Backend Subagent]
        BE1[Design APIs & Data Models]
        BE2[Implement Backend Logic]
    end

    subgraph RUN[Code Execution & Integration]
        I[Integrate Frontend + Backend]
        R[Run & Test Application]
    end

    subgraph V[Verification Subagent]
        V1[Validate Against User Requirements]
        V2{Requirements Met?}
    end

    U --> P
    P --> Q
    Q -- Yes --> A --> P
    Q -- No --> FE1

    FE1 --> FE2 --> BE1
    BE1 --> BE2 --> I
    I --> R --> V1
    V1 --> V2
    V2 -- No --> P
    V2 -- Yes --> D[Deliver Solution]
```
