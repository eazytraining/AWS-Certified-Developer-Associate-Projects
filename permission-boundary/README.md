# AWS IAM Permission Boundaries Lab

### 📝 Description  
This lab demonstrates how to use **AWS IAM Permission Boundaries** to enforce the principle of least privilege. You will create a boundary policy to limit the maximum permissions of an IAM user, even if their attached policies grant broader access.  

**Scenario**:  
A financial company ("SecureBank") needs to ensure developers can only perform read-only actions on S3 and EC2, even if their IAM policies accidentally grant full access.  

---

### 🎯 Objectives  
- Create a **permission boundary** policy to restrict S3 and EC2 actions.  
- Attach the boundary to an IAM user with overly permissive policies.  
- Validate that the boundary blocks destructive actions (e.g., deleting S3 buckets).  

---

### 📋 Prerequisites  
- An AWS account with IAM access.  
- AWS CLI installed and configured (use `aws configure` for an admin profile).  

---

### 🛠️ Lab Steps  

#### 1. Create the Permission Boundary Policy  
Create a policy that allows only **read-only actions** on S3 and EC2.  

#### 2. Create an IAM User with Overly Permissive Policies
Create a user policy granting full S3/EC2 access, then attach the boundary.
#### 3. Test the User's Permissions
Use the AWS CLI to verify the boundary restricts permissions.



