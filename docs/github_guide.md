# GitHub: A Complete Guide

## What is GitHub?

GitHub is a **cloud-based platform** built on top of Git that provides hosting for software development and version control. While Git is a tool you run locally on your computer to track changes in code, GitHub is a web service that lets you store your Git repositories online, collaborate with others, and access a suite of tools designed for software teams.

Think of it this way: **Git** is the engine, **GitHub** is the car — it makes that engine accessible, social, and collaborative.

GitHub was founded in 2008 and acquired by Microsoft in 2018. It is now home to over 100 million developers and more than 300 million repositories, making it the world's largest platform for open-source software.

---

## Core GitHub Concepts

### Repositories (Repos)

A **repository** is the fundamental unit of GitHub. It is a project's home — containing all the project's files, folders, and the complete history of every change ever made to them.

Repositories can be:

- **Public** — visible to anyone on the internet
- **Private** — visible only to you and collaborators you explicitly invite

Every repository has a unique URL in the format:

```
https://github.com/username/repository-name
```

#### Key parts of a repository page:

- **Code tab** — Browse files and folders
- **Issues** — Bug reports and feature requests
- **Pull Requests** — Proposed changes awaiting review
- **Actions** — Automated workflows (CI/CD)
- **Settings** — Repository configuration

#### Creating a Repository

1. Click the **+** icon in the top-right corner of GitHub
2. Select **New repository**
3. Enter a repository name (e.g., `my-project`)
4. Choose **Public** or **Private**
5. Optionally check **Add a README file**
6. Click **Create repository**

---

### Forking

**Forking** creates your own personal copy of someone else's repository under your GitHub account. The fork is fully independent — you can make any changes you like without affecting the original project. However, it maintains a connection to the original (called the **upstream**) so you can pull in updates or submit your changes back via a Pull Request.

Forking is the backbone of open-source contribution on GitHub. If you want to contribute to a project you don't own, you fork it, make your changes, and propose them back.

#### How to Fork a Repository

1. Navigate to the repository you want to fork on GitHub
2. Click the **Fork** button in the top-right corner of the page
3. Select your account (or an organisation) as the destination
4. GitHub creates a copy at `https://github.com/your-username/repository-name`

That's it — you now own a copy of that repository.

#### Keeping Your Fork Up to Date

Over time, the original repository may receive new commits. To sync your fork:

```bash
# Add the original repo as a remote called "upstream"
git remote add upstream https://github.com/original-owner/repository-name.git

# Fetch the latest changes from upstream
git fetch upstream

# Merge upstream changes into your local main branch
git checkout main
git merge upstream/main

# Push the updated branch to your fork on GitHub
git push origin main
```

---

### Cloning

**Cloning** downloads a copy of a repository from GitHub to your local machine so you can work on it. Unlike forking (which happens on GitHub), cloning happens on your computer via the terminal.

You can clone any repository you have access to — your own, a fork, or a collaborator's.

#### How to Clone a Repository

1. Navigate to the repository on GitHub
2. Click the green **Code** button
3. Copy the URL (HTTPS is easiest for beginners; SSH is recommended for regular use)
4. Open your terminal and run:

```bash
git clone https://github.com/username/repository-name.git
```

This creates a new folder called `repository-name` in your current directory containing all the project files.

#### Clone into a specific folder name

```bash
git clone https://github.com/username/repository-name.git my-folder-name
```

#### Cloning via SSH (recommended for frequent use)

First, [add your SSH key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), then:

```bash
git clone git@github.com:username/repository-name.git
```

---

### Pull Requests (PRs)

A **Pull Request** is a proposal to merge changes from one branch (or fork) into another. It is the primary mechanism for code review and collaboration on GitHub.

When you open a Pull Request, GitHub shows a diff of your changes, allows teammates to leave comments, request changes, or approve the PR. Once approved, it can be merged.

#### How to Open a Pull Request

1. Push your changes to a branch on GitHub (either your fork or the same repo)
2. Navigate to the original repository on GitHub
3. Click **Pull requests** → **New pull request**
4. Select the **base branch** (where changes should go) and your **compare branch** (your changes)
5. Add a clear title and description explaining _what_ and _why_
6. Click **Create pull request**

---

### Issues

**Issues** are GitHub's built-in task tracker. They are used to report bugs, request features, ask questions, or track any work that needs to be done on a project.

Issues support Markdown formatting, labels, assignees, and milestones, making them a lightweight project management tool.

#### Creating an Issue

1. Navigate to a repository and click the **Issues** tab
2. Click **New issue**
3. Write a descriptive title and detailed body
4. Optionally assign labels (e.g., `bug`, `enhancement`, `help wanted`) and an assignee
5. Click **Submit new issue**

---

### GitHub Actions

**GitHub Actions** is GitHub's built-in automation and CI/CD (Continuous Integration / Continuous Deployment) platform. You define workflows in YAML files that automatically run in response to events — like pushing code, opening a pull request, or on a schedule.

Common uses:

- Running tests automatically on every push
- Deploying your app when code is merged to `main`
- Linting and formatting checks
- Sending notifications

Workflow files live in `.github/workflows/` within your repository.

---

### GitHub Pages

**GitHub Pages** lets you host a static website directly from a GitHub repository — for free. It's commonly used for project documentation, personal portfolios, and open-source project sites.

#### Enabling GitHub Pages

1. Go to your repository's **Settings**
2. Scroll to the **Pages** section in the left sidebar
3. Under **Source**, select the branch to deploy from (e.g., `main`)
4. Click **Save**
5. Your site will be live at `https://your-username.github.io/repository-name`

---

### Stars and Watching

- **Starring** a repository bookmarks it and shows appreciation to the author. Your starred repos are accessible from your profile.
- **Watching** a repository subscribes you to notifications for all activity — issues, PRs, comments, etc.
- **Forking** (see above) creates your own copy to work from.

---

### GitHub Gists

**Gists** are a lightweight way to share snippets of code or notes. Each Gist is a mini repository that can be public or secret, and can contain one or more files. Find them at [gist.github.com](https://gist.github.com).

---

### Organisations and Teams

**Organisations** are shared accounts that allow groups of people to collaborate across many repositories. Within an organisation, **Teams** can be created to manage permissions — for example, a `frontend` team might only have access to certain repos.

---

## Forking vs. Cloning — What's the Difference?

|                            | Forking                                      | Cloning                                        |
| -------------------------- | -------------------------------------------- | ---------------------------------------------- |
| **Where it happens**       | On GitHub (in the cloud)                     | On your local machine                          |
| **What it creates**        | A copy of the repo under your GitHub account | A local copy of the repo on your computer      |
| **Connected to original?** | Yes — can sync updates and open PRs          | Only if you add it as a remote manually        |
| **When to use it**         | Contributing to a project you don't own      | Working on a project you own or collaborate on |

In practice, you often do **both**: fork a repo on GitHub, then clone _your fork_ to your local machine.

```bash
# 1. Fork on GitHub (click the Fork button)
# 2. Clone your fork locally
git clone https://github.com/your-username/repository-name.git

# 3. Add the original as "upstream"
git remote add upstream https://github.com/original-owner/repository-name.git
```

---

## Quick Reference: Common GitHub Workflows

````

### Starting a New Project

```bash
# 1. Create a repo on GitHub
# 2. Clone it locally
git clone https://github.com/your-username/new-project.git
cd new-project

# 3. Add files, commit, and push
git add .
git commit -m "Initial commit"
git push origin main
````

---

## Further Reading

- [GitHub Docs](https://docs.github.com) — Official documentation
- [GitHub Skills](https://skills.github.com) — Interactive learning courses
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow) — GitHub's recommended branching workflow
