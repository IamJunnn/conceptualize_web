import os

# Define the base directory where you want to create the demo
BASE_DIR = "Conceptualize_Demo"

# Define the folder structure and files with their content
demo_structure = {
    "Classes/CS 101 - Intro to Programming": {
        "Algorithms.md": """# Algorithms

Key concepts from today's lecture:

- **Sorting algorithms**: Bubble sort, Quick sort
- **Search algorithms**: Binary search, Linear search
- **Time complexity**: Big O notation

## Application Ideas
Could use [[Data Structures]] to optimize search functionality for [[AI Study Buddy]]

The concept of recommendation algorithms might be useful for [[StudyConnect]] - matching students with similar learning goals.
""",
        "Data Structures.md": """# Data Structures

## Key Concepts
- Arrays and Lists
- Hash Tables
- Trees and Graphs
- Stack and Queue

## Real-world Applications
Graph structures could model connections between:
- Students helping each other
- Concepts in different courses
- Related [[Project Ideas]]

💡 Idea: Use graph database for [[StudyConnect]] to show knowledge connections between users!

See also: [[Algorithms]]
""",
        "Final Project Ideas.md": """# CS 101 Final Project Ideas

## Options:
1. **Task Management App** - Basic CRUD app
2. **Study Group Matcher** - Could be the MVP for [[StudyConnect]]!
3. **Campus Event Calendar**

## Chosen Direction
Going with #2 - the study group matcher. This connects perfectly with:
- [[Business Model Canvas]] from entrepreneurship class
- [[Customer Discovery]] insights
- [[Technical Architecture]] plans

Links to [[Project Overview]]
"""
    },
    "Classes/ECON 201 - Microeconomics": {
        "Supply and Demand.md": """# Supply and Demand

## Class Notes - Week 3

Key insights:
- Market equilibrium
- Elastic vs Inelastic demand
- Price sensitivity

## Application to [[StudyConnect]]

Student time is **scarce** (supply)
Exam season creates **high demand** for study help

Could implement dynamic pricing? Or keep it free and monetize differently?

See: [[Pricing Strategies]], [[Revenue Model]]
""",
        "Market Research.md": """# Market Research

## Methods Learned:
1. Surveys
2. Focus groups
3. Competitor analysis
4. Customer interviews

## Applied to My Project
Did [[Customer Discovery]] interviews with 15 students last week!

Key findings:
- 80% struggle to find study partners
- 60% feel classes are disconnected from each other
- Students want to see how concepts relate across subjects

This validates the core value prop of [[StudyConnect]]
""",
        "Pricing Strategies.md": """# Pricing Strategies

## Types:
- Cost-plus pricing
- Value-based pricing
- Freemium model
- Subscription

## For [[StudyConnect]]:
Leaning toward **freemium**:
- Free: Basic matching
- Premium: AI-powered study recommendations, cross-course connections

Related: [[Revenue Model]], [[Supply and Demand]]
"""
    },
    "Classes/MGMT 301 - Entrepreneurship": {
        "Business Model Canvas.md": """# Business Model Canvas

## 9 Building Blocks:

### Customer Segments
- College students (18-24)
- Focus on STEM majors initially
- See [[Target Market]] for details

### Value Proposition
Connect students across courses to:
- Form study groups
- See how knowledge connects
- Learn collaboratively

### Channels
- Campus ambassadors
- Instagram/TikTok
- Word of mouth

### Revenue Streams
See [[Revenue Model]] - freemium approach

### Key Resources
- [[Technical Architecture]]
- [[Data Structures]] and [[Algorithms]]
- Student network

### Key Activities
- [[Customer Discovery]]
- Product development
- Community building

Full project: [[Project Overview]]
""",
        "Lean Startup Method.md": """# Lean Startup Method

## Core Principles:
1. Build-Measure-Learn loop
2. MVP (Minimum Viable Product)
3. Validated learning
4. Pivot or persevere

## Applying to [[StudyConnect]]:

### MVP Features:
- Simple profile creation
- Manual study group matching
- Basic course tagging

### Hypotheses to Test:
1. Students want cross-course connections
2. Graph visualization adds value
3. Willing to pay for premium features

### Next Steps:
See [[Next Steps]] for MVP timeline

Related: [[Customer Discovery]]
""",
        "Customer Discovery.md": """# Customer Discovery

## Interview Summary (Week of Oct 15)

### Interviewed: 15 students

### Key Pain Points:
1. **Hard to find study partners** (13/15 mentioned)
2. **Classes feel isolated** - no connection between subjects (11/15)
3. **Don't know who's taking similar courses** (9/15)
4. **Existing apps are too complex** (7/15)

### Quotes:
> "I wish I could see how my econ class relates to my CS class"

> "GroupMe is cluttered. I just want to find one good study partner"

### Insights for [[StudyConnect]]:
- **Simplicity is key**
- **Visual connections matter** - students love the graph idea!
- **Cross-discipline learning** is underserved

See: [[Market Research]], [[Aha Moment]]
"""
    },
    "Project Ideas": {
        "Campus Food Delivery App.md": """# Campus Food Delivery App

## Concept:
DoorDash but only for campus dining halls and nearby restaurants

## Pros:
- Clear revenue model
- Existing demand

## Cons:
- Very competitive market
- High operational complexity
- Doesn't leverage my unique insights

**Status**: Shelved for now. Focusing on [[StudyConnect]] instead.
""",
        "AI Study Buddy.md": """# AI Study Buddy

## Concept:
AI chatbot that helps you study by:
- Generating practice questions
- Explaining concepts
- Creating study guides

## Inspiration:
From [[Algorithms]] class - thinking about recommendation systems

## Pros:
- Hot market (AI)
- Clear value proposition

## Cons:
- Highly competitive (ChatGPT, etc.)
- Requires significant AI expertise

## Pivot Idea:
What if I combined this with social features? → [[StudyConnect]]

Students learn better together + AI can enhance connections
""",
        "Sustainable Campus Store.md": """# Sustainable Campus Store

## Concept:
Thrift store for textbooks, supplies, dorm items

## Status: Backlog

Not pursuing right now, but keeping for later.
"""
    },
    "Active Projects/StudyConnect": {
        "Project Overview.md": """# StudyConnect - Project Overview

## Tagline:
*"See how your classes connect. Learn with others who think like you."*

## The Problem:
Students learn in silos. Classes feel disconnected. It's hard to find study partners who "get it."

## The Solution:
StudyConnect helps students:
1. **Visualize** how their courses and concepts connect
2. **Find** study partners based on shared interests and complementary knowledge
3. **Learn** collaboratively across disciplines

## Origin Story:
Started as [[Final Project Ideas]] for CS 101. Validated through [[Customer Discovery]]. Built on principles from [[Business Model Canvas]] and [[Lean Startup Method]].

## Core Innovation:
Using [[Data Structures]] (graph database) to model:
- Students → Nodes
- Shared courses/interests → Edges
- Concept connections → Meta-edges

Visual inspiration from knowledge graphs.

## Current Status:
Building MVP. See [[Next Steps]].

Related docs:
- [[Target Market]]
- [[Technical Architecture]]
- [[Revenue Model]]
""",
        "Target Market.md": """# Target Market

## Primary Segment:
**College students (18-24), STEM-focused**

### Why STEM first?
- Clear concept connections between courses
- Students already think in systems
- High adoption of tech tools
- Personal network for initial testing

## Student Personas:

### 1. "Cross-Disciplinary Carla"
- Double major (CS + Business)
- Sees connections everywhere
- Wants to apply concepts across fields
- **Pain**: Feels like knowledge is fragmented

### 2. "Struggling Steve"
- Engineering major
- Works hard but feels isolated
- Wants study partners but doesn't know who
- **Pain**: Can't find people who explain things his way

### 3. "Ambitious Amy"
- Pre-med, takes tough courses
- Competitive but collaborative
- Wants efficient study methods
- **Pain**: Wastes time on ineffective study groups

## Market Size:
- 20M college students in US
- 40% in STEM fields = 8M
- TAM: $500M+ (if $5/month premium x 10% adoption)

From [[Market Research]] and [[Business Model Canvas]]
""",
        "Technical Architecture.md": """# Technical Architecture

## Tech Stack:

### Frontend:
- React + TypeScript
- D3.js for graph visualization
- Tailwind CSS

### Backend:
- Node.js + Express
- GraphQL API

### Database:
- Neo4j (graph database) - perfect for modeling connections!
- PostgreSQL for user data

### Auth:
- Firebase Auth (quick MVP)

## Key Features:

### 1. Profile Creation
- Courses taken/taking
- Interests and goals
- Learning style

### 2. Graph Visualization
- Force-directed layout (from [[Data Structures]] class!)
- Interactive: zoom, pan, click
- Different node colors for different course types

### 3. Matching Algorithm
Uses concepts from [[Algorithms]]:
- Similarity scoring
- Collaborative filtering
- Graph traversal for "friends of friends"

### 4. Connection Discovery
- See which classmates have overlapping interests
- Find cross-course connections
- Suggest study topics based on graph clusters

## MVP Scope:
- Manual profile input
- Basic graph view
- Simple keyword matching

## Future (Premium Features):
- AI-powered recommendations
- Automated course extraction
- Study session scheduling

Related: [[Project Overview]], [[Next Steps]]
""",
        "Revenue Model.md": """# Revenue Model

## Strategy: Freemium

### Free Tier:
- Create profile
- Basic graph view of your courses
- Find study partners (limit 5 matches/week)
- Join study groups

### Premium Tier ($4.99/month):
- Unlimited matching
- AI-powered study recommendations
- Cross-course concept mapping
- Advanced graph analytics
- Priority support
- Study session scheduling

## Revenue Projections:
Based on [[Target Market]] research:
- Year 1: 1,000 users → 100 premium (10%) = $500/month
- Year 2: 10,000 users → 1,000 premium = $5,000/month  
- Year 3: 50,000 users → 5,000 premium = $25,000/month

## Alternative Revenue:
- B2B: Sell to universities for $10k-50k/year
- Sponsored study materials
- Tutoring marketplace (take commission)

From [[Pricing Strategies]] and [[Supply and Demand]] analysis
""",
        "Next Steps.md": """# Next Steps - Sprint Planning

## This Week (Oct 21-27):
- [x] Finish [[Customer Discovery]] interviews
- [ ] Finalize [[Technical Architecture]]
- [ ] Design database schema
- [ ] Create wireframes

## Next 2 Weeks (Oct 28 - Nov 10):
- [ ] Build MVP backend
- [ ] Implement graph visualization
- [ ] Basic matching algorithm
- [ ] User authentication

## Month 2 (November):
- [ ] Beta testing with 20 students
- [ ] Iterate based on feedback
- [ ] Refine [[Revenue Model]]

## Month 3 (December):
- [ ] Launch to 100 students
- [ ] Implement premium features
- [ ] Campus ambassador program

From [[Lean Startup Method]] and [[Business Model Canvas]]
"""
    },
    "Journal": {
        "2024-10-15 Aha Moment.md": """# 2024-10-15 - Aha Moment! 💡

Today in [[ECON 201 - Microeconomics]] we were discussing network effects, and it just clicked!

The professor said: *"The value of a network grows exponentially with each new user"*

That's when I realized - [[StudyConnect]] isn't just a study tool. It's a **knowledge network**. 

Every student who joins adds:
1. Their unique course combinations
2. Their way of understanding concepts
3. New connections between ideas

The more diverse the students, the more valuable the connections!

This is exactly what I learned about [[Data Structures]] - graphs become more interesting with more nodes and edges.

## Next Actions:
- Update [[Project Overview]] with network effects angle
- Revise [[Target Market]] - diversity is key!
- Think about growth strategy

Related: [[Customer Discovery]], [[Business Model Canvas]]
""",
        "Weekly Reflections.md": """# Weekly Reflections

## Week of Oct 14-20, 2024

### Wins:
- Completed 15 [[Customer Discovery]] interviews
- Strong validation for [[StudyConnect]] concept
- Made connections between [[Algorithms]] and real business problems
- Had [[Aha Moment]] about network effects

### Challenges:
- Balancing coursework with project development
- Need to learn more about [[Technical Architecture]]
- Time management

### Key Learnings:
- Cross-disciplinary thinking is my superpower
- Students WANT to see connections between classes
- Simple beats complex every time

### Next Week Goals:
1. Finalize [[Technical Architecture]]
2. Start building MVP
3. Apply [[Lean Startup Method]] principles
4. Keep detailed notes in all classes - they connect!

### Courses Connecting This Week:
- CS 101 → StudyConnect tech foundation
- ECON 201 → Business strategy
- MGMT 301 → Entrepreneurship framework

This is exactly what StudyConnect should show!
"""
    }
}

def create_demo_structure():
    """Create all folders and markdown files"""
    
    # Create base directory
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        print(f"✅ Created base directory: {BASE_DIR}")
    
    # Create all folders and files
    for folder_path, files in demo_structure.items():
        # Create the full folder path
        full_folder_path = os.path.join(BASE_DIR, folder_path)
        os.makedirs(full_folder_path, exist_ok=True)
        print(f"📁 Created folder: {folder_path}")
        
        # Create each file in the folder
        for filename, content in files.items():
            file_path = os.path.join(full_folder_path, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ Created file: {filename}")
    
    print(f"\n🎉 Demo structure created successfully in '{BASE_DIR}' folder!")
    print(f"\n📊 Summary:")
    print(f"   - Total folders: {len(demo_structure)}")
    total_files = sum(len(files) for files in demo_structure.values())
    print(f"   - Total files: {total_files}")
    print(f"\n💡 Next step: Open '{BASE_DIR}' folder in Conceptualize!")

if __name__ == "__main__":
    create_demo_structure()