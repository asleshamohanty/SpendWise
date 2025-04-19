# SpendWise: AI-Driven Financial Behavior Modification

## Problem Statement

Young adults face significant challenges when it comes to managing their finances. With easy access to one-click shopping, subscription traps, and impulse-driven purchases influenced by social media, it's no wonder that saving and budgeting are often pushed to the backburner. Despite various budgeting tools available, most are passive — they only show what has already happened, after the damage is done.

The result?  
- **Monthly budgets are blown by the 10th.**  
- **Savings are always "next month's" priority.**  
- **Guilt replaces financial goals.**

This leads to financial stress, low confidence in savings, and the inability to meet long-term goals, such as building investments, creating emergency funds, or even going on vacations.

## Our Solution: Make Money Talk — Literally

SpendWise is an AI-powered financial assistant designed to help young adults make smarter financial decisions. Unlike traditional budgeting apps that merely track expenses, SpendWise actively helps users prevent impulsive spending, predict balances, and manage their finances effectively.

### Key Features

1. **Smart Nudges**  
   Our AI assistant alerts users when they are about to make impulsive financial decisions. These notifications are based on users’ spending history, habits, and context. Over time, these nudges become increasingly personalized and aware of the user’s behavior.

2. **Finance Advisor Chatbot**  
   Not sure if a purchase is impulsive? Ask the in-built AI chatbot! It provides practical, personalized insights to help users understand their spending patterns and psychology, empowering them to make better financial choices.

3. **ML-Based Impulsive Expense Prediction**  
   Using machine learning, our model predicts impulsive expenses and flags them before they occur. This helps users take preventive action, and the more users interact with the system, the more the model evolves to become highly accurate.

4. **Balance Prediction**  
   Predict your future account balance! Based on your current spending patterns and savings rate, SpendWise can forecast your balance at the end of the month, helping you plan better and avoid unpleasant surprises. This allows you to make informed decisions on where you can cut back or save more.

5. **Gamified Financial Challenges**  
   Saving money can be fun! We gamify the experience by introducing challenges, streaks, and rewards for staying within budget or hitting savings goals. It's financial wellness, but with a twist.

6. **Financial Score**  
   A dynamic scoring system that evaluates how well the user is adhering to their financial goals and savings targets, giving them a tangible measure of progress.

---

## Tech Stack

### Frontend
- **React**: Used for building a responsive and dynamic UI for the user to interact with the system.
- **Chatbot Interface**: Integrated within the frontend using React components.

### Backend
- **Express.js**: A RESTful API that serves as the core logic handler for communication between the frontend, machine learning models, and the database.
- **MongoDB**: A NoSQL database used to store user profiles, expenses, nudges, savings history, and financial progress.

### Machine Learning & Chatbot
- **Python (Flask)**: Handles the machine learning model that predicts impulsive spending, balance forecasting, and offers savings suggestions.
- **Custom AI Chatbot**: Built using Python and Flask, the chatbot educates users about financial behaviour and provides personalised spending advice.

---

## Impact and Future Directions

### Impact
- **Financial Control**: Users feel empowered and motivated to manage their finances better.
- **Engagement & Positive Behavior**: Gamification and the chatbot make the traditionally stressful task of managing money more engaging and enjoyable.
- **Higher Savings Confidence**: Early testers have shown improved saving habits and increased daily engagement.

### Future Directions
1. **Bank Balance Connection**: Integration with bank APIs for automatic balance fetching, eliminating manual data entry, and providing real-time insights.
2. **Enhanced Gamification**: Badges, levels, and interactive visuals to make saving and budgeting more fun and engaging.
3. **Emotionally Intelligent Chatbot**: Future development to enhance the chatbot with emotion-aware responses for a more personalized, supportive experience.
4. **Progress Rewards**: Milestone celebrations with rewards to motivate users and encourage consistency.
5. **Personalised Challenges & Streaks**: Tailored challenges and streak systems to help users build sustainable and long-term financial habits.

---

## Getting Started

### Prerequisites
- Node.js (for frontend and backend)
- Python (for machine learning and chatbot)

### Installation Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/SpendWise.git
    cd SpendWise
    ```

2. **Setup Backend**:
    ```bash
    cd SpendWise-Backend
    npm install
    npm start
    ```

3. **Setup Frontend**:
    ```bash
    cd SpendWise-Frontend
    npm install
    npm start
    ```

4. **Setup Machine Learning**:
    ```bash
    cd SpendWise-ML
    pip install -r requirements.txt
    python app.py
    ```

---

## Hackathon Project

SpendWise was our team project for the Codeathon 2025 (Hackathon by Manipal Institute of Technology), where we placed **#6** among numerous talented participants. Our goal was to create an AI-driven financial assistant that not only helps users track their expenses but also helps them build healthier financial habits through machine learning, balance prediction, and behavioural nudges. The project aims to provide young adults with the tools they need to manage their money in a fun, engaging, and proactive way.

---

## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository, make changes, and submit a pull request.

**SpendWise** is an innovative project that leverages AI to empower users with the tools they need to manage their finances better. Whether it's saving for the future, avoiding impulsive purchases, predicting balances, or setting financial goals, our platform is designed to be your financial assistant, every step of the way.
