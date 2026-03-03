# Markdown Writing Guide

### A Complete Introduction for Absolute Beginners

---

## What Even Is Markdown?

Imagine you're writing a text message, but instead of tapping a "Bold" button, you just wrap the word in `**asterisks**` and it automatically becomes **bold**. That's Markdown — a simple set of symbols you type into plain text to control how it looks when displayed.

You write this:

```
**Hello**, world!
```

The reader sees this: **Hello**, world!

That's it. No special software. No formatting toolbar. Just plain text with a few punctuation tricks.

Markdown is used **everywhere**: GitHub, Reddit, Notion, Slack, WhatsApp, Discord, Jupyter Notebooks, documentation sites, blogs, and more. Learning it once pays off endlessly.

---

## Why Should You Learn It?

- ✅ Works in almost every modern writing tool
- ✅ Your files are plain `.txt` — they open anywhere, forever
- ✅ Faster than reaching for your mouse to click formatting buttons
- ✅ Looks clean and professional with zero design effort
- ✅ Easy to learn in one sitting

---

## Part 1 — Headings

Headings let you create titles and section names. You make them by starting a line with one or more `#` symbols. More `#` symbols = smaller heading.

**You write:**

```markdown
# Big Title (like a book title)

## Chapter Heading

### Section Heading

#### Sub-section

##### Smaller still

###### Smallest heading
```

**Rules to remember:**

- Always put a space between the `#` and your text: `# Hello` ✅ not `#Hello` ❌
- Use `#` (H1) only once per document — it's your main title
- Use `##` and `###` to organize sections and sub-sections

---

## Part 2 — Bold, Italic, and Strikethrough

| What you want | What you type            | Result     |
| ------------- | ------------------------ | ---------- |
| Bold          | `**word**` or `__word__` | **word**   |
| Italic        | `*word*` or `_word_`     | _word_     |
| Bold + Italic | `***word***`             | **_word_** |
| Strikethrough | `~~word~~`               | ~~word~~   |

**Examples:**

```markdown
This is **really important**.
This is just _slightly_ important.
This is **_extremely_** important.
This feature is ~~deprecated~~ removed.
```

---

## Part 3 — Lists

### Unordered Lists (bullet points)

Use `-`, `*`, or `+` before each item:

```markdown
- Apples
- Bananas
- Oranges
```

### Ordered Lists (numbered)

```markdown
1. Wake up
2. Make coffee
3. Open laptop
4. Write some Markdown
```

### Nested Lists (lists inside lists)

Indent with 2 or 4 spaces:

```markdown
- Fruits
    - Apples
    - Bananas
- Vegetables
    - Carrots
    - Broccoli
```

### Task / Checklist (GitHub, Notion, Obsidian)

```markdown
- [x] Buy groceries
- [x] Write README
- [ ] Deploy the app
```

---

## Part 4 — Links and Images

### Links

The format is: `[text you see](URL)`

```markdown
Visit [Google](https://google.com) for more info.
```

It shows like this (which is clickable): [Google](https://google.com)

### Images

Almost identical to links, but with a `!` at the start. The text in `[]` is the "alt text" — shown if the image fails to load.

```markdown
![A cute cat](https://example.com/cat.jpg)
![Local chart](images/chart.png)
```

![cute_cat](sample_images/cute_cat.jpg)

## Part 5 — Code

### Inline Code

Wrap in backticks `` ` `` for short snippets:

```markdown
Use the `print()` function to display output.
Run `npm install` in your terminal.
```

### Code Blocks

Use three backticks before and after. Name the language for syntax highlighting:

````markdown
```python
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```
````

Common language tags: `python`, `javascript`, `bash`, `html`, `css`, `sql`, `json`

---

## Part 6 — Blockquotes

Use `>` to highlight important notes or quotes:

```markdown
> This is a blockquote. Use it to highlight important information.

> Outer quote
>
> > Inner quote (nested)
```

---

## Part 7 — Tables

Use `|` to separate columns and `-` to create the header divider:

```markdown
| Name   | Role      | Country |
| ------ | --------- | ------- |
| Alice  | Developer | USA     |
| Bob    | Designer  | UK      |
| Carlos | Manager   | Spain   |
```

**Column alignment** — add `:` to the divider row:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| text |  text  |  text |
```

---

## Part 8 — Horizontal Rules

Use three or more `---` on their own line:

```markdown
Some content above

---

Some content below
```

---

## Part 9 — Escaping Special Characters

Use a backslash `\` to show a character literally instead of formatting:

```markdown
This is \*not italic\*.
I want to show a \# without making a heading.
```

Characters you may need to escape: `\ * _ # [ ] ( ) ! > | ~`

---

## Quick Reference Cheat Sheet

```
# H1 Heading          ## H2 Heading          ### H3 Heading

**bold**              *italic*               ***bold italic***

~~strikethrough~~     `inline code`

- bullet item         1. numbered item        - [x] task item

[link text](URL)      ![alt text](image URL)

> blockquote

| Col 1 | Col 2 |     ---  (horizontal rule)
|-------|-------|
| cell  | cell  |

\* escape special characters with backslash
```

---

## Common Mistakes to Avoid

| ❌ Mistake                             | ✅ Fix                                             |
| -------------------------------------- | -------------------------------------------------- |
| `#Heading` — no space                  | `# Heading` — always add a space                   |
| Text immediately after a heading       | Leave a blank line between headings and paragraphs |
| Forgetting the `!` for images          | `![alt](url)` — the `!` is what makes it an image  |
| Mixing tabs and spaces in lists        | Stick to spaces (2 or 4) for indentation           |
| Closing a code block on the wrong line | Make sure the closing ` ``` ` is on its own line   |

---

## Where to Practice

- **[dillinger.io](https://dillinger.io)** — Live preview in your browser, no signup needed
- **[markdownlivepreview.com](https://markdownlivepreview.com)** — Side-by-side editor and preview
- **[GitHub](https://github.com)** — Any `README.md` file renders Markdown automatically
- **Notion, Obsidian, VS Code** — All support Markdown natively

---

## You're Ready

You now know everything you need to write clean, well-structured Markdown. The best way to learn is to start using it — open any of the practice tools above and try rewriting a few notes in Markdown format.

Before long, typing `**bold**` will feel as natural as hitting Ctrl+B ever did.
