# Project Proposal
## CMP 315: Secure Software Engineering<br><br>**BSc Cybersecurity Year 3**<br><br>2023/24


## **Document Control**

| Date | Version | Changes by | Notes |
| ---- | ---- | ---- | ---- |
| 19/02/2024 | 1.0 | Ewan Taylor | First draft of proposal |
|  |  |  |  |



# Contents

 [1     Executive summary.](#1-executive-summary)</br>
 [2     Project Overview.](#2-project-overview)</br>
    [2.1       Project Introduction.](#21-project-introduction)</br>
    [2.2       Project Stakeholders](#22-project-stakeholders)</br>
    [2.3       Project Methodology.](#23-project-methodology)</br>
    [2.4       Group Roles](#24-group-roles)</br>
[2.5       Project Scope and Milestones](#25-project-scope-and-milestones)</br>
[3     Requirements 5](#3-requirements-5)</br>
    [3.1       Functional Requirements](#31-functional-requirements)</br>
    [3.2       Non-Functional Requirements](#32-non-functional-requirements)</br>

# 1 Executive summary

As part of the Secure Software Engineering module (CMP315), all Cybersecurity students have been tasked as a group to develop a software project that utilises secure software engineering practices. Following discussion and agreement as a cohort, this proposal proposes the development of [Project Name], an open-source password manager, as it allows for the embedding of secure software engineering techniques and integrating them within the software development lifecycle.

The primary goal of [Project Name] is to improve cybersecurity etiquette and simplify password management for individuals and small organisations, with the potential for medium-scale expansion. To achieve this, user credentials will be required to be encrypted and stored in a secure manner in a system resilient to attack vectors, whilst also remaining user-friendly and readily accessible.

# 2   Project Overview

## 2.1  Project Introduction

[Project Name] addresses the ever-continuing need for robust, secure password management in an increasingly digital world. By utilising software engineering and web application pen testing skills learned in CMP307 and CMP319 respectively, the team aims to develop a password manager that emphasizes security, usability, and accessibility.

The project will follow the software development lifecycle (SDLC), incorporating continuous testing and feedback to ensure a finished product where security has been at the heart of development throughout the entire process.

## 2.2  Project Stakeholders

The project will be completed by the third-year Cybersecurity undergraduate cohort (six students) each contributing with their own skillset and experience throughout the development of the project. Further stakeholders include academic staff assisting with the delivery of the module and providing support with the project where applicable. All stakeholders can be found in the table below.

| **Name** | **Stakeholder Type** |
| ---- | ---- | ---- |
| Ewan Taylor | Student | 
| Ryan Van Ee | Student | 
| Liam Morgan | Student | 
| Jack Barnett | Student | 
| Liam Townsley | Student | 
| Owen Walker | Student | 
| Shailendra Rathore | Academic Staff | 
| Ian Ferguson | Academic Staff | 

## 2.3  Project Methodology

Based on experience with prior modules, the decision was made to manage this project using an agile methodology. This approach allows us to embrace flexibility, an iterative development process and make changes dynamically based on feedback from our lecturing staff and testing. Since the size of the group developing this project is relatively small, this allows us to communicate frequently both in-person and online, which allows for an agile approach to be adopted effectively. With this approach, the aim is to ensure that we create a password manager adopting secure software engineering practices throughout the software development life cycle.

Team roles will be clearly defined, with responsibilities allocated based on individual strengths and interests.

## 2.4  Group Roles

[Roles at present are subject to change]

| **Role** | **Responsibilities** | **Name** |
| ---- | ---- | ---- |
| **Project Manager** | Oversees project schedules, outputs, and dialogue with stakeholders. Produces and updates project records for clear and open access to project details and progress. | Ewan Taylor |
| **Front-End Developer** | Crafts and refines the user interface with C#, ensuring it's user-friendly, secure and visually appealing. | Tbc |
| **Back-End Developer** | Constructs the application's server-side framework, centring on server, logic, and database operations using Python. Guarantees safe data management and streamlined server-side functionalities. | Tbc |
| **System Integration & DevOps Developer** | Integrates application parts, including the user-facing and server-side elements. Creates and handles automation for continuous integration and deployment, improving development efficiency and update rollouts. | tbc |
| **Security & Quality Assurance Engineer** | Implements security measures and leads exhaustive tests to spot vulnerabilities. Confirms the application functions as desired and is resilient to attacks. | tbc |
| **Database & Encryption Specialist** | Manages database architecture with an emphasis on data security through encryption. Works in tandem with the back-end developer to protect and secure user information. | tbc |

## 2.5  Project Scope and Milestones

[Scope and Milestones are subject to change]

### **Scope:**

The scope of [Project Name] encompasses the development of an open-source password manager focusing on encryption, user interface design, and cross-platform compatibility. This initiative aims to enhance cybersecurity practices by securely encrypting and storing user credentials in a system that is not only resistant to common cyber threats but also maintains ease of use and accessibility across different platforms

### **Milestones**:

- Requirements analysis/ Research Phase
- Design
- Implementation / Prototype Development
- Testing (unit and integration)
- Deployment
- Final Release

# 3   Requirements

[Project Name] is guided by a clear set of functional and non-functional requirements, emphasising secure software engineering practices and usability.

## 3.1  Functional Requirements

**FR1:** The system shall allow users to securely store and manage login credentials for various websites and applications.

**FR2:** The system shall provide a feature for generating strong, unique passwords for users.

**FR3:** Users must be able to edit or update their stored login credentials.

**FR4:** Users shall be able to delete their stored credentials.

**FR5:** Each set of credentials will be automatically assigned a unique identifier within the system.

**FR6:** The system will employ AES encryption to secure all stored credentials.

**FR7:** Users shall have the option to categorise credentials (e.g., social, financial, work).

**FR8:** The system shall connect to a secure, encrypted database for storing encrypted credentials and user information.

**FR9:** The database shall store user profile information, including name and email address.

**FR10:** The system shall feature a user-friendly interface for managing passwords and account settings.

**FR11:** The system must authenticate users with an email address and a master password before allowing access to stored credentials.

**FR12:** The system shall provide secure and encrypted synchronization of credentials across user devices.

**FR13:** The system shall offer users the ability to import and export their credentials in a secure manner.

**FR14:** The system must support plugins or extensions for web browsers to facilitate auto-filling of login forms.

**FR15:** Users should be able to search their stored credentials by website, username, or category.

**FR16:** The system must provide an emergency access feature for trusted contacts in case the primary user is unable to access their account.

**FR17:** The system shall support multi-factor authentication for user login to enhance security.

**FR18:** The system shall implement security measures to detect and alert users of potential password breaches or reuse.

## 3.2  Non-Functional Requirements

**NFR1:** The system should ensure minimal latency in credential retrieval and management operations.

**NFR2:** User instructions and guidance should be clear, concise, and easily accessible within the application.

**NFR3:** The system must be designed for cross-platform compatibility, including desktop and mobile platforms.

**NFR4:** System updates and backups should be conducted securely and efficiently without interrupting the user experience.

**NFR5:** The system must adhere to best practices in data security and privacy, including compliance with relevant standards and regulations.

**NFR6:** The architecture should be scalable to accommodate a growing number of users and credentials without performance degradation.

**NFR7:** The system must implement robust error handling and logging mechanisms to quickly address and resolve issues.

**NFR8:** The design and development process should incorporate continuous testing, including unit tests, integration tests, and security penetration tests.

**NFR9:** Accessibility features should be incorporated to ensure the system is usable by individuals with varying abilities.

**NFR10:** The system must maintain high availability and reliability, with strategies in place for disaster recovery and data loss prevention.
