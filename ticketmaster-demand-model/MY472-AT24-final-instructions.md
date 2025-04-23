# MY472: Final Take-Home Assessment (summative)

### Autumn Term 2024

### Deadline: Wednesday, 15th January 2025, 17:00 London time

--- 

### _Data science is about bringing clarity to ambiguous situations_

Inside and outside academia, one of the most important skills of a data scientist is to be able to take an ambiguous set of instructions and generate a work product that brings structure and clarity to other people, such as your manager or other academics reviewing your work. This is one of the major themes of this course. We have purposefully pushed you to think creatively, troubleshoot problems on your own, and complete assessments with less guidance than you were probably used to as an undergraduate student. In our view, success in this course is _not_ about how well you can regurgitate lines of code; it is about well you can manage an ambiguous situation and generate useful, impactful and reproducible work.

For this final assessment, you will complete an **_independent data science report_**. The report should accompany new real-world data, which you will compile, clean and organise on your own using the skills you have learned in this course. As you will see below, this assessment is more open-ended than the previous assessments; this is on purpose. It is now your turn to demonstrate you have learned how to bring clarity to ambiguous situations, and that you are ready to take on the work of a data scientist. 

---

### Overview

You should select **one** of the **3 options** given below to be the "prompt" for your project. These prompts are purposefully broad and you will have to decide how best to narrow the scope to meet the requirements of the assessment. You will then compile and use data relating to your prompt, summarising it in a report. A future person should be able to read your report, fully understand your process, fully reproduce your work, and use your dataset for their own research project. You must produce new _real-world_ data.

**Prompt 1:** Pretend that you have just started a new job as a junior data scientist at a public policy think tank. The think tank is growing and becoming more influential, so your manager has asked you to compile new data relating to an important public policy problem, which could be used by the think tank to prepare future analyses. You have _not_ been asked to complete these analyses; your primary task is to produce the new data and prepare a report that introduces it and justifies why the data is important and promising.
 
**Prompt 2:** Pretend that you are a PhD student in social science discipline. You are working with your supervisor to put together a grant to fund a new social science research project. Your supervisor has asked you to compile new data relating to your primary research interest, which could be used to write a future article analysing the data. You have _not_ been asked to write an article analysing the data; your primary task is to produce the new data and prepare a report that introduces it and justifies why the data is important and promising.

**Prompt 3:** Pretend that you are a junior data scientist that has just been hired to a professional job by a large organisation (e.g., a company, a foundation, a government, a university, etc.). You were hired because the organisation is struggling to meet it core objective (e.g., hitting a revenue target, increasing enrolment, etc.). Your boss has asked you to compile new data that the organisation could analyse in order to better understand why its objectives aren't being met. You have _not_ been asked to complete these analyses; your primary task is to produce the new data and prepare a report that introduces it and justifies why the data is important and promising.

Your work must be submitted in a GitHub repository that includes your written report in both `Rmd` format and a professional, knitted `html`, as well as your new data and supporting files. As usual, the work in your `Rmd` file **must be reproducible from start to finish**.

--- 

### Structure of the report

Your report must be organised into exactly six sections using the Rmarkdown template we have provided (`MY472-AT24-final-report.Rmd`), which should be knitted to html upon completion of your work. You should _not_ alter the name or location of this file in your GitHub repository. In the template, anything inside square brackets can and should be replaced with your own words and work. At the beginning of your report, you must indicate which prompt you chose (see the template for details). Each section must begin with a section heading that is numbered and titled appropriately based on the template. Please do not use the following section descriptions as the titles for your sections; your titles should make sense for your project. 

In each section, you should include the text of your report, as well as the code you used. For this assessment, we will _not_ be using a code appendix. However, the text and the code must make sense together---each section should be neat, professional and organised to be easily readable. All of your code will be evaluated based on how neat and organised it is, and whether you appropriately used the coding techniques we taught in this course.

<!-- Q: Is the section easily readable? -->

Your report must have exactly six sections, as follows:

#### 1. A concise and engaging introduction

You should begin your report with a concise and engaging introduction. At a minimum, this introduction should describe the data you are collecting, why it is important and interesting, and what it could be used for. Your introduction should also narrow the scope of the prompt in a way that is both clear and engaging to the reader. For example, if you choose prompt 3, your introduction should make clear what organisation you work for and what objective it is struggling to meet. Your introduction does _not_ need to include an outline the remaining sections of your report, as this would be a waste of space.

#### 2. Retrieving your primary data

In this section, you should describe and retrieve the primary raw data for your report. You should explain what data you are collecting, how you are collecting it and why it can be considered your "primary" data. You should include all code to reproduce your results, organised neatly as described in more detail below. This data _must_ be automatically sourced from the web, meaning that you must use R code to get it onto your computer. You cannot use data that is not publicly accessible (e.g., behind a paywall), nor can you _manually_ click and download (if needed, `RSelenium` is ok). The data need not be in tabular format, and indeed, many interesting data sources will not be. However, you will need to create/use tabular data in sections 5 and 6 below. 

You should explain whether there are any limits on the data you collected, and how you complied. You should also describe any ethical concerns or considerations in your data collection  (e.g., when web scraping) and how you dealt with that in your code to ensure a responsible workflow. 

#### 3. Retrieving your secondary data

In this section, you should describe and retrieve secondary data. You should provide a good explanation for why it is supplements the primary data, and how you envision it could be used to augment the primary data. When we evaluate your data collection in sections 2 and 3, we want to see that you have used a broad range of techniques from this course. This means you may wish to collect different _types_ of data for sections 2 and 3, but it is not necessary. As before, you should include all code to reproduce your results, organised neatly as described in more detail below. This data _must_ be automatically sourced from the web, meaning that you must use R code to get it onto your computer. You cannot use data that is not publicly accessible (e.g., behind a paywall), nor can you _manually_ click and download (if needed, `RSelenium` is ok).

You should explain whether there are any limits on the data you collected, and how you complied. You should also describe any ethical concerns or considerations in your data collection  (e.g., when web scraping) and how you dealt with that in your code to ensure a responsible workflow. 

#### 4. Tabular data and transformations

In this section, you need to first demonstrate that you have built tidy tabular data that can be used for future analyses. If your data is not already tidy tabular data, you should create tidy tabular data here. Then, you need to make at least five _meaningful_ transformations, which have to be _in addition to_ any transformations you needed to do to retrieve or organise data in previous sections. This could include making new variables, significant changes to variable formatting (i.e., not simply changing the R data type), etc. Please enumerate and briefly explain the five transformations in text (i.e., don't just give the code and ask us to interpret it).

#### 5. Use the data

In this section, you need to present the data in a compelling fashion. You should do this in two different ways. You should present your data using tools and techniques from the course. The purpose of this section is two fold: (1) give your reader a nice orientation to the data you have collected, and (2) to demonstrate to the reader the potential for learning new things from the data. You should ask yourself: what do you want the reader to see? As usual, you should provide all your code and describe (and concisely justify) what you are doing.

#### 6. Data and output storage 

You must store your data in at least two different ways. This includes both your raw data (e.g., texts) and any derivative data you create (e.g., tabular data). You must also store any "outputs" you create in or for your report, especially in part 5. Your choices about how to store your data will be partly evaluated on how organised and portable your resulting storage system is. (By "portable" we mean: how easy it is for others to recreate and/or clone the storage system in their own workspace.)

You must also replace the contents of the `README` file in your GitHub repository with concise information about the data you collected, and how it is organised in the repository. Do not include lots of details in this README; only the basic information that will help someone know how what's in the repository and how it is organised.

--- 

### Formatting and style requirements

##### General considerations

You must create an organised and professional "report" with supporting files. Your report must show your work, explain what you are doing, write in full sentences, structure your document for readability, etc. Part of our evaluation of your assessment will consider how professional, clear and organised your work is.

##### Word limit

Your report must not include more than 1,000 words of text (and preferably less than 800). Your code chunks do not count against this word limit, but you will lose marks if we think you have tried to sneak more words into your report by writing _excessively_ long comments inside your code chunks or _excessively_ verbose and repetitive code. This is a very tight word limit; you will need to be clear, concise and to-the-point.

Note: the word count feature in RStudio does not exclude code chunks. In order to check how many words you have written (excluding code chunks), you can use the following R script:

```{r, eval=FALSE}
library(tidyverse)

rmd_file <- "tba" # path to your Rmd file

read_file(rmd_file) %>% # read the file as a text file
  str_squish() %>% # remove all extra white space
  str_replace("^.+?output.+?[-]{3}", "") %>% # remove header
  str_replace_all("```[{].+?```", " ") %>% # remove code chunks
  str_replace_all("<![-].+?-->", " ") %>% # remove rmd comments
  str_replace_all("[!]?\\[.+\\][(].+[)]", " ") %>% # remove links
  str_replace_all("(^|\\s+)[^A-Za-z0-9]+", " ") %>% # remove symbols (1)
  str_replace_all("[^A-Za-z0-9]+($|\\s+)", " ") %>% # remove symbols (2)
  str_count("\\S+") %>% 
  paste("The document is", ., "words.") %>%
  print()
```

##### Directory and file management

You should organise and name your files appropriately. Do not change the location or the name of the template `Rmd` you will use for your report. In all of your code, you should use good "directory management" practices that allow another user to easily reproduce your work with minimal directory set up. See some examples from seminar exercises. Your GitHub repository should be neatly organised, with subdirectories for large amounts of data and/or output files, as needed. 

If you have very large files, you may not be able to save them to GitHub (see [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)). In that case, please use another cloud storage service for the large files and provide access to the instructors. Your report should make it easy for the reader to access (e.g., by using a download function on a link you've shared). Note: you should ONLY do this for large files you cannot practically store in GitHub; other work, including your report, should still be stored in your GitHub repository.

##### Code chunks

All code chunks should be "appropriately modular" meaning that each chunk should complete a self-contained part of the task, and it should make sense why you broke up the chunks way you did. You should neither use a separate chunks for every line of code, nor should you _necessarily_ have one big code chunk for a section. Most importantly: the way you break up the chunks needs to make sense in context and make your report more readable.  

You should also:

- Label each code chunk using a unique, informative (but very short) label
- Use the defaults for `eval` and `echo`, unless a particular line generates a lot of output. If you set `echo=FALSE` or `eval=FALSE` for any chunk, please explain why
- Write your code to avoid excessive output; only show the most important information, and be sure to only show enough output to be useful
- Comment your code concisely; explain steps in a way that a reader would find useful
- Your entire project (including all outputs) should be reproducible; anything that cannot be traced back to your code will not be marked

##### Getting data from the web

You will partly be evaluated based on how creative and novel your new data is.

All webscraping and API use should use the good etiquette we developed in this class, including using `if()` tests to check if data has already been scraped/saved to avoid redundant scraping. A reader should be able to re-compile **with _or_ without** re-doing the scraping you previously did. You should also check that you are not violating any terms of any website you scrape or otherwise access. 

**Under _no_ circumstances can you ever scrape data from any LSE Library database or resource.**

##### Use of ChatGPT or other AI

You can use ChatGPT to help you with coding tasks or phrasing, but you cannot use it to generate chunks of code that fully complete your tasks, or to generate large amounts of written text. In your courses, unless otherwise specified, you should _never_ be using ChatGPT or other AI tools to generate sentences of text or large chunks of code that you copy/paste.

If you used ChatGPT to help you in any way, please explain at the beginning of the document. If you use ChatGPT or AI to produce a small amount of code (to fix a specific problem, for example), then it should be commented in the following way (beginning your AI disclosure comment with `### * `):

```{r, eval=FALSE}
### * the following lines of code were generated by AI/ChatGPT 
fakefun <- function(x){
  # a fake function for illustration
  print("You should use ChatGPT/AI sparingly, if at all!")
}
```

Please keep in mind that we can usually tell when code or text has been generated from ChatGPT or other AI. If we suspect that there was inappropriate use of these tools, we will mark accordingly.^[For example, if there is a lot of code that does not look like code we used in this course and there is not adequate explanation for it.] Egregious uses of these tools will be considered academic misconduct and will be handled according to LSE's disciplinary procedures (see below).

--- 

### Questions about the assessment

We will not take any questions about this assessment. This is because we are partly evaluating you on your ability to "bring clarity to an ambiguous situation" by producing an _independent_ data science report. At this point in the course, all students should have have gained the skills to do well on this assessment, assuming they have devoted sufficient time and energy to learning and reviewing the course material.

--- 

### Submission logistics using GitHub Classroom

For all assessments in MY472, you will need to submit your solutions via GitHub Classroom using a Git/GitHub workflow like you have seen in lecture and seminar.

When you clicked on the assignment link that I sent in a course announcement, it would have automatically created a private repo in your GitHub account. We refer to this as your "Submission Repo" for this assessment. It initially includes this README file, as well as a template file you will use to write your report (`MY472-AT24-final-report.Rmd`).

Your Submission Repo is _private_. It is where you will store your work and it is where we will collect your answers after the deadline. There is no official "submission" process in GitHub Classroom: simply work on your files in your Submission Repo freely until the deadline. Please note that after the deadline, you should no longer make any changes to your Submission Repo, and you may be automatically blocked from doing so by GitHub. Instructors automatically have access to your repo.

After you complete the exercises _but before the deadline_, you should do the following:

1. Knit (to HTML) your report in your local copy of your Submission Repo.
2. Commit and push the final versions of all your work contained in your local copy of your Submission Repo.
3. Visit your Submission Repo on <https://www.github.com> to ensure all the files are the versions you intend to submit.

**_All your files and folders must be committed and pushed to GitHub/remote before the deadline._** 

##### Some fair warnings about submitting your answers correctly

Your mark for every assessment will be based on what the markers are able to see in your Submission Repo, so _please, please, **PLEASE** do not forget to commit and push your changes to remote on GitHub and check the files on GitHub are up-to-date_. Corrupted, illegible, missing, renamed, or otherwise damaged files will not be marked. We will only mark the last versions of your files that were committed and pushed before the deadline. We will not contact you to correct any problems with the files in your Submission Repo. It is your responsibility to ensure you submit your work correctly. Failure to do so will cause you to receive zero marks and no feedback. 

**Please note that if your `MY472-AT24-final-report.Rmd` and `MY472-AT24-final-report.html` files have been moved or renamed, or you did not use the template correctly, your report will not be marked.**

--- 

### Anonymity and marking

Please do not put any personally identifiable information (such as your name) inside any file that you include in your Submission Repo, except for your LSE candidate number. Every assessment is marked anonymously, meaning that the marker will not know who you are, assuming that you have followed our instructions *not* to include personally identifiable information in any file in your Submission Repo.

For every assessment, you will be asked to put your LSE candidate number on the top of your answers file. We will track your progress in the course using your LSE candidate number.

You may choose to submit your assessments under your main, personal GitHub account or another "anonymised" account that you create for the purposes of submitting assessments in MY472. Please note that even if you choose to use your personal GitHub account, your solutions will still be marked anonymously, as the course convenor will anonymise each students’ submission before allocating them among the course markers.

--- 

### Extensions

We will not ordinarily grant extensions to individual students unless:

1. You have a pre-approved adjustment or accommodation and have requested an extension.

2. You have formally requested an extension from the Department and it has been granted. Please see the Assessments section of the Moodle page to review the Department’s extension policies and procedures.

If you have been granted an extension through either of these two processes, you must inform the course instructors ASAP so that they can modify your deadline in GitHub Classroom. To do so, please forward any email you receive from the Department to the convenor within 1 day of receiving it.

--- 

### Academic integrity

You may not collaborate with others on this assessment. Any work you submit for this assessment must be your **own original and independent work**.

While you may use outside resources and/or chatbots like ChatGPT for support, but you must cite all sources and clearly and explain how you used any chatbots to arrive at your answers. See above for more information.

If anyone or anything (e.g. ChatGPT) **_substantially_** completes your solutions on your behalf, this will no longer be considered your own original and independent work and will be considered academic misconduct.

More generally, it should go without saying that plagiarism, unauthorised collaboration, re-using prior work, and fabrication of data are all serious breaches of academic integrity and constitute violations of LSE's policies. The instructors actively monitor the integrity of student assessments, and suspected violations of LSE policies will be investigated and referred for disciplinary measures as appropriate. 

Keep in mind that a student's lack of awareness about the expectations for academic integrity at LSE is _not_ a valid defence against an allegation of academic misconduct. So, if you are unfamiliar with the norms and expectations around academic integrity at LSE, please review them here:  <https://info.lse.ac.uk/current-students/services/assessment-and-results/exams/exam-discipline-and-academic-misconduct>.
