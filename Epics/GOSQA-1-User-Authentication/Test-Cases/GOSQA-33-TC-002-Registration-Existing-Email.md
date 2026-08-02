# GOSQA-33 – TC-002: Verify Registration Fails When Using an Existing Email Address

## Epic

**GOSQA-1 – User Authentication**

---

## Related Story

**GOSQA-26 – Register a New User Account**

---

## Objective

Verify that the system prevents user registration when the email address is already registered.

---

## Preconditions

- GOSQA-34 – User is not logged in.
- GOSQA-35 – Registration page is accessible.
- GOSQA-36 – An account already exists with the target email address.

---

## Test Steps

| Step | Action | Test Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Open the registration page. | URL: `/register` | Registration page is displayed successfully. |
| 2 | Enter a unique username. | `hamed_new` | Username is accepted. |
| 3 | Enter an email address that is already registered. | `existing@example.com` | Email address is accepted for validation. |
| 4 | Enter a valid password. | `Password123!` | Password is accepted. |
| 5 | Confirm the password. | `Password123!` | Password confirmation matches the original password. |
| 6 | Click the **Register** button. | — | Registration request is submitted. |

---

## Expected Result

- The registration request is rejected.
- No new user account is created.
- An appropriate validation message is displayed indicating that the email address is already in use.

---

## Traceability

### Related Story

- GOSQA-26 – Register a New User Account

### Related Preconditions

- GOSQA-34
- GOSQA-35
- GOSQA-36

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
- Test: **GOSQA-33**