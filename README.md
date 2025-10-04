# Cloud Cost Calculator 

A real-world AWS project that helps businesses understand, track, and optimize their cloud costs.  
Instead of confusing AWS bills, this project provides **clear dashboards, cost alerts, and automated weekly reports**.

---

## 🚨 Problem

Businesses often get **unexpected and confusing AWS bills**.  
- Different services charge differently (by hour, gigabyte, request, etc.).  
- Companies waste money without realizing where it’s going.  
- No visibility → no optimization.  

Example: A company expecting a $10,000 bill suddenly receives a $30,000 invoice — with no idea why.

---

## ✅ Solution

I built a **Cloud Cost Calculator** system that:  
1. **Tracks spending automatically** across AWS services.  
2. **Sends cost alerts** when spending crosses thresholds.  
3. **Provides a dashboard** that explains costs in simple categories.  
4. **Generates weekly reports** comparing this week vs last week.

---

## 🏗️ Architecture

**AWS Services Used:**
- **CloudWatch** → Collects spending metrics & creates alarms.  
- **SNS (Simple Notification Service)** → Sends email/SMS alerts when thresholds are exceeded.  
- **S3 (Static Website Hosting)** → Hosts a simple cost dashboard.  
- **Lambda** → Generates weekly reports and uploads to S3.  

**Flow Diagram:**
