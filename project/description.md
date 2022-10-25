
# Group Project Assignment


## Learning Goals
In parallel to working towards the general learning objectives of the Advanced Machine Learning Course, you are intended to

- Solve an interesting problem,
- Implement and apply a recent machine learning method,
- Evaluate and report the method performance.


## Timeline - Overview
* Wed, 09.11. Deadline for your own project description xor choice of pre-defined project
* Tue, 10.11. Project Kick-Off (after the lectures)
* Thu, 24.11. Supervision meeting (mandatory)
* Thu, 08.12. Group presentation round (mandatory)
* Tue, 03.01.2023 Project report hand-in (mandatory)
* Tue-Wed, 24.-25.01.2023 Oral exams (includes your project)


## Formalities
As seen in the timeline, the project time is 11.11.-08.12., so roughly four weeks. 
  During this time you have no lectures or other mandatory exercises for the course, but the opportunity to discuss some rework of previous lectures/exercises (if needed) and the (optional) exercise sheet 10 during the exercise time on 15.11. 

However, the final report is due on 3rd of January 2023. The project work is done in groups of 2–4 people. The group formation happens via LearnIT, and you need to register as one group until 09./10.11.2022.

You can start the project at any point earlier if this better fits your schedule (given your group and project are settled), but there will be no extensions for the mandatory group presentation or report submission.


## Problem Statement
To reach our learning goals, your task as a group is to:

* understand a chosen problem, select appropriate (existing and recent) dataset(s), and understand feasible existing solutions (the *state of the art*), 
* select and implement (at least) one machine learning method - as a general rule, you may take code pieces from existing repositories/exercises/papers as long as you understand and can explain that code, and cite it, 
* evaluate and report your solution for appropriate measure w.r.t. your chosen problem (e.g. accuracy/performance, edge cases, model behaviour) - and discuss/reflect peculiar strengths and weaknesses.

As optional additional steps, we highly encourage you to (and/or):
* expand a solution with your own original ideas, 
* transfer your solution onto different datasets (potentially from different domains),
* experiment with novel approaches to add insight/explainability about the models' decisions.

For this, you can either select one of the prepared projects below or create your own.

#### Prepared projects

* [Detection of distracted drivers](p_distracted_drivers.md)
* [Estimation of Psychlogical and/or Physiological Information](p_psychophysiological_study.md)
* [Fake News Detection](p_fakenews.md)
* [Human Motion Analysis for Automatic Feedback](p_fitness.md)
* [Image segmentation with deep encoder-decoder networks](p_image_segmentation.md) 
* [Modelling how the brain represents visual information](p_brainvision.md)
* [Tagging music sequences](p_music_tagging.md)
* ...

#### Create your own project
You are encouraged to come up with your own project and propose it to the teachers (contact Stella). Good inspirations for your own project are:

* [**Kaggle**](https://www.kaggle.com/competitions), 
* [**paperswithcode.com**](https://paperswithcode.com/) 
* [IEEE openaccess datasets](https://ieee-dataport.org/datasets)
* [Google Dataset Search](https://datasetsearch.research.google.com/search?query=cats)

... or a problem that you encountered in other courses and found **particularly motivating**. In your proposal, roughly orient yourself on the format of the prepared projects above and describe:

1. Title of the project and people of the group,
2. Key problem and/or research question,
3. Short (!) paragraph of context - outline existing appropriate datasets and how the problem is generally approached (e.g. with which ML paradigm/method-family),
4. List 3-5 main goals that guide your project, according to the problem statement above,
5. List *n* optional goals that you find particularly interesting (e.g. attempt better ideas than found in the state of the art).


## Supervision meeting
This supervision meeting is an individual session with one teacher for you as a group.
Therein we want to hear about your current open questions and challenges, and thereby help you resolve roadblocks and guide you towards a successful finalized project.
## Supervision
We plan to guide you with supervision and mentoring during the project to help you develop ideas and approaches, to resolve roadblocks, and to guide you towards a successful finalised project.

1. Our TA is there for all ideas/questions/problems on **Tuesdays 14-16h** (or longer if needed) in 3A54 and/or online.

2. We organise a **supervision meeting** halfway (on **24.11.** between 12-14h) as an individual session between one of the teachers and your group. We will organise a slot of about 30min per group with a schedule beforehand (in LearnIT). The meeting is about helping you with your current open questions and challenges - code or results can be discussed but are not required.


## Group presentation round
The aim for the presentation round in class (during the last lecture/exercises slots of the semester) is to inform each other about your experiences and to focus your project work on one key outcome. Thus, we organise the group presentation round as a mini-conference. 
The aim for the presentation round in class (during the last lecture/exercises slots of the semester, **08.12.** from 12h ct onwards) is to inform each other about your experiences and to focus your project work on one key outcome. Thus, we organise the group presentation round as a mini-conference. 

Each project group is asked to:
* provide a 7 min. presentation + 3 min. Q/A - it is recommended to limit to 5 slides or a live notebook,
* give highlights of your project:
  * central problem,
  * central methods,
  * key results,
  * most important and interesting lesson learned;
* focus on the audience! Thus inform and motivate your fellow students of our AML course,
* ideally: (be prepared to) demonstrate the model/experiment/evaluation live in class for interesting discussions.

Additionally, one student from the last presenting group moderates the next presenting group (thus, one student from the last group moderates the first group), which means:
* help with the set up and announce the presentation,
* help a bit with the time keeping,
* facilitate the Q/A round.


## Project report hand-in 
You must hand in both a report (see below) and the source code you have developed to solve the project. For each group, only one person should hand in the project (report and code).

#### Implementation and Code
Your implementation has to be in Python. You may make use of any standard Python libraries and the numerical libraries NumPy and SciPy, as well as machine learning frameworks such as PyTorch or Tensorflow. 
Your code should be organised such that is easy to read, i.e. you have to use descriptive names for files, functions, variables, etc. The code may be organised in regular Python source files (.py files) or in Jupyter notebooks. If you take inspiration from or copy code developed by other people, it is important that you document this in your report. Your code must be handed in as a single file (either a zip or tar archive). A good submission would be Jupyter notebook with crisp documentation inline and all blocks being run.

#### Report
Please provide your report in pdf format. We provide a two-column template [here](https://www.overleaf.com/read/zcmpjrvfqpsg), which you should use for your report, which must be no longer than a total of 6 pages, including figures, tables, (psoudo-)code snippets, but excluding references and appendixes. 
Note that the hand-in should be self-contained, although you are required to be able to explain your code for the oral exam. Your oral presentation during the exam should correspond to the structure of your write-up. 

The report should consist of the following sections. The goal is to be crisp, informative, and interesting, while providing the necessary facts and arguments from your experimentation. 
1. Introduction. Here you provide the context for the problem and re-state it briefly.
2. Methods. Here you define and describe your methods, with precise mathematics where applicable.
3. Experiments. Here you describe your data source and provide the numerical results of your method over the data. The results refer to the quantitative and qualitative evaluations that you need to carry out.
4. Discussion. Here you reflect and discuss the results against the original question's setting and the results published in the scientific article selected. Here you also discuss peculiar strengths and short-comings
of the methodology/data and argue for potential future work.
5. Conclusions. Here you provide a couple of sentences summarising the results of the project and the indicated future improvements.
6. References. This is a numbered reference list of the works you cite in the report, of the key methods referred. This section is not counted in the page limit.

#### Honesty Codex 
By submitting your project, you confirm that you have not submitted this project elsewhere and that you did not copy (plagiarise) foreign content without proper reference. If you use someone else's work, you must cite and refer to it properly. 


## What if "it does not work"?
First of all: Don't panic. This happens all of the time! Maybe a better line of questions is: What? It works? Are you a wizard?

In research, we often try things which do not work, i.e. we fail, sometimes even spectacularly (but please don't put our HPC on fire). This will not at all make you fail your project or this course. We want you to reflect and understand. Don't hide your failures. Learn from them and give your fellow students a chance to learn from you.

Let's assume you try something which does "not work out". In this case, your task is, among other things, to describe what made you conclude this. There may be many reasons for failure, e.g. a method you re-implemented yields different results than the reference, or your proclaimed "improved" model performs worse than the baseline model, or your model does not converge in training, etc.  
* Why do you claim "it does not work"? 
* What can be possible reasons for this?
* Additionally: perform additional experiments to support your hypothesis of "why did it fail"?

