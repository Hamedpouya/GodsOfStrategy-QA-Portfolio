# GOSQA-40 – TC-004: Verify Successful Login with Valid Credentials

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-27 – Authenticate Users and Provide Account Access**

---

## Objective

Verify that a registered user can successfully log in using valid credentials.

---

## Preconditions

- GOSQA-43 – A registered user account exists.
- GOSQA-44 – User is logged out.
- GOSQA-45 – Login page is accessible.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the login page. | URL: `/login` | Login page is displayed successfully. |
| 2 | Enter a valid username. | `hamed123` | Username is accepted. |
| 3 | Enter the correct password. | `Password123!` | Password is accepted. |
| 4 | Click the **Login** button. | — | Authentication request is submitted successfully. |

---

## Expected Result

- Authentication is successful.
- The user is granted access to the account.
- The user is redirected to the home page or dashboard.

---

## Traceability

### Related Story

- GOSQA-27 – Authenticate Users and Provide Account Access

### Related Preconditions

- GOSQA-43
- GOSQA-44
- GOSQA-45

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
- Test: **GOSQA-40**