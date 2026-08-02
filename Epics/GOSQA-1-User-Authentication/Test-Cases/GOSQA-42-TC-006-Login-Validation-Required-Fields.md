# GOSQA-42 – TC-006: Verify Login Validation When Required Fields Are Empty

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-27 – Authenticate Users and Provide Account Access**

---

## Objective

Verify that the system validates required fields and prevents login when mandatory inputs are missing.

---

## Preconditions

- GOSQA-46 – User is on the login page.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the login page. | URL: `/login` | Login page is displayed successfully. |
| 2 | Leave the username field empty. | Username: Empty | Username field remains blank. |
| 3 | Leave the password field empty. | Password: Empty | Password field remains blank. |
| 4 | Click the **Login** button. | — | Login request is blocked and validation is triggered. |

---

## Expected Result

- Login request is not submitted.
- Validation messages are displayed for all required fields.
- The user remains on the login page.

---

## Traceability

### Related Story

- GOSQA-27 – Authenticate Users and Provide Account Access

### Related Preconditions

- GOSQA-46

---

## Priority

Highest

---

## Status

Completed

---

## Jira Reference

- Epic: **GOSQA-1**
- Story: **GOSQA-27**
- Test: **GOSQA-42**