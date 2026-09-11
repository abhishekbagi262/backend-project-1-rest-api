# Backend Project 1 – REST API Fundamentals

## 📌 Project Overview

This project is a simple REST API built using Python and Flask.

The purpose of this project is to understand REST API fundamentals, including HTTP methods, routing, JSON data, and stateless communication.

## 🛠️ Technologies Used

- Python
- Flask
- REST API
- JSON
- HTTP

## 🚀 API Endpoints

### GET `/`

Returns a welcome message from the API.

### GET `/hello`

Returns a simple success message.

### POST `/users`

Accepts user details in JSON format and returns the submitted data.

**Required fields:**
- `name`
- `course`

If required fields are missing, the API returns a `400 Bad Request` response.

## 🧪 API Testing

### GET `/`

**Request:**

```text
GET http://127.0.0.1:5000/