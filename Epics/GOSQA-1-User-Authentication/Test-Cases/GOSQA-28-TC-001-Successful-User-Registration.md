# GOSQA-28 – TC-001: Verify Successful User Registration with Valid Information

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-26 – Register a New User Account**

---

## Objective

Verify that a new user can successfully register an account using valid registration information.

---

## Preconditions

- GOSQA-29 – User is not logged in.
- GOSQA-30 – Registration page is accessible.
- GOSQA-31 – Username and email address are not already registered.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the registration page. | URL: `/register` | Registration page is displayed successfully. |
| 2 | Enter a unique username. | `hamed123` | Username is accepted. |
| 3 | Enter a valid email address. | `hamed@example.com` | Email address is accepted. |
| 4 | Enter a valid password. | `Password123!` | Password is accepted. |
| 5 | Confirm the password (if applicable). | `Password123!` | Password confirmation matches the original password. |
| 6 | Click the **Register** button. | — | Registration request is submitted successfully. |

---

## Expected Result

- Registration is completed successfully.
- A new user account is created.
- The user is redirected to the appropriate page (dashboard, home page, or login page depending on the system design).
- No validation or system error messages are displayed.

---

## Traceability

### Related Story

- GOSQA-26 – Register a New User Account

### Related Preconditions

- GOSQA-29
- GOSQA-30
- GOSQA-31

---

## Priority

Highest

---

## Status

Completed

---

## Jira Reference

- Epic: **GOSQA-1**
- Story: **GOSQA-26**
- Test: **GOSQA-28**