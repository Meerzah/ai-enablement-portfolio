# IT Operations Prompt Playbook

Starter prompts for the IT Ops team using the internal AI helpdesk agent.
Last updated: 2025

---

## Runbook queries

**Find troubleshooting steps**
```
I'm seeing [error message / symptom]. What are the troubleshooting steps 
in our runbooks for this?
```

**Summarize a runbook**
```
Summarize the MDM enrollment runbook for a new Mac. Give me the steps 
as a numbered list I can paste into a ticket.
```

**Check if a process is documented**
```
Do we have a runbook for [process name]? If yes, what does it cover?
```

---

## Identity and access queries

**Check group membership**
```
Who is currently in the [group name] Okta group?
```

**Check a user's access status**
```
Is [email address] active in Okta? When did they last log in?
```

**Audit a user's groups**
```
What Okta groups does [email address] belong to?
```

---

## Ticket drafting

**Draft an incident summary**
```
Based on this timeline: [paste timeline], write a 3-sentence incident 
summary for the ticket. Include what happened, what was affected, 
and what resolved it.
```

**Draft a user communication**
```
Write a short Slack message to [team name] letting them know [system/tool] 
will be unavailable on [date] from [time] to [time] for maintenance. 
Keep it under 4 sentences.
```

---

## Policy and compliance

**Look up a policy**
```
What is our policy on [topic]? Summarize the key points and any 
exceptions mentioned.
```

**Check a procedure**
```
What is the correct procedure for [action, e.g. offboarding a contractor]?
List the steps in order.
```

---

## Tips

- Be specific about names, dates, and systems — the agent uses exact terms to search
- If an answer seems off, ask: "Which document did that come from?"
- Add new prompts that work well to this list and share in #it-ai-tools
