ALUMNI CONNECT

Software Requirements Specification  Document

Project Name: Alumni Connect
Version: 1.0
Prepared by: AINAMANI DICKSON
                   OFWONO GODWIN
                   ATUHAIRE ABIUDI
Date: 21st March,2025

1. Introduction

1.1 Purpose
	This Alumni Connect is a Web based Application designed to provide a platform where alumni of an institution can register, log in and interact with other alumni. 
This system facilitates networking among Alumni, collaboration on ongoing projects in the institution, tracking of on going events at the institution and access to institutional latest news.

1.2 Scope
This system allows alumni to:
    • Create an account and log in.
    • View profiles of other alumni Members.
    • Check and participate in ongoing projects.
    • Get updates on institution-related news and events.
    • Engage in discussions and activities within their current community.
This system is built using HTML, CSS for front-end, Django for back-end and SQLite3 as the database. 
It is a web-based application accessible via desktop and mobile browsers.

1.3 Stakeholders
    • Alumni – These are the primary users who register and interact with the platform.
    • Institution Administration – They manage alumni data, news and events ongoing in the institution.
    • Developers – This is our team maintaining and updating the system.

1.4 References
    • Django Official Documentation
    • SQLite3 Database Documentation
    • Web Accessibility Guidelines

2. Overall Description

2.1 Product Features
    • User Authentication :  Secure login and registration.
    • Profile Picture:  Users can update their profiles with relevant details.
    • Members :  A list of registered alumni with profile information Is displayed on Members Page.
    • News :  Institutional updates and event notifications.
    • Activities :  Section to showcase alumni-led initiatives.
    • Logout : Member signs out of the system.

2.2 Constraints
    • This system must run on modern web browsers.
    • Uses SQLite3 as a database which may need migration for scalability.
    • Requires stable internet access.

2.3 Assumptions and Dependencies
    • Users have basic knowledge of web navigation.
    • The institution will provide the necessary alumni data for verification.

3. System Requirements
3.1 Functional Requirements
    • Users can register and log in securely.
    • Users can edit and view profiles.
    • Users can browse other alumni profiles.
    • Admins can post news, events and updates.

3.2 Non-Functional Requirements
    • Security: Encrypted passwords and role-based access.
    • Performance: System should load within 3 seconds under normal usage.
    • Scalability: Should support a large number of users as alumni grow.
    • Usability: Simple and intuitive UI for easy navigation.

4. External Interface Requirements
4.1 User Interfaces
    • Login Page – Allows users to sign in/register.
    • Dashboard – Displays Members,news, activities,logout and profile nav bars.
    • Members – Lists all registered users with search functionality.

4.2 Hardware Interfaces
    • This system should runs on devices with at least 2GB RAM and a modern browser.

4.3 Software Interfaces
    • Front-end : HTML, CSS
    • Back-end : Django
    • Database : SQLite3

4.4 Communication Interfaces
    • HTTPS for secure communication.

5. Validation & Deployment
5.1 Validation Criteria
    • All users should be able to register and log in.
    • Members page should display accurate details.
    • Admin functionalities (news/events posting) should work as expected.

5.2 Deployment Plan
    • Containerize using Docker for easy deployment.
    • Use GitHub Actions for CI/CD.
    • Future migration from SQLite3 to PostgreSQL for scalability.

6. Change Management
    • Track feature requests and bug fixes via GitHub Issues.
    • Regular security updates and performance enhancements.

Thank You