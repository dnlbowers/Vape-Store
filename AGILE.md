# Agile Methodology

## **Table of Contents**

* [Agile Methodology](#agile-methodology)
  * [Overview](#overview)
  * [Sprint Notes](#sprint-notes)
    * [Sprint 1 Notes](#sprint-1-notes)
    * [Sprint 2 Notes](#sprint-2-notes)
    * [Sprint 3 Notes](#sprint-3-notes)
    * [Sprint 4 Notes](#sprint-4-notes)
    * [Sprint 5 Notes](#sprint-5-notes)
    * [Sprint 6 Notes](#sprint-6-notes)
    * [Sprint 7 Notes](#sprint-7-notes)
    * [Sprint 8 Notes](#sprint-8-notes)

## Overview

After using [JIRA](https://dnlbowers.atlassian.net/jira/software/projects/PVS/boards/5/roadmap) for [my last project](https://github.com/dnlbowers/jobs-a-gooden) to track my sprints, I decided to use it again for this project over git hub issues. JIRA has many more built-in features, such as analytics which assist me in sprint planning and review.

I split all user stories into several epics and linked each story, task, or bug fix ticket to the related epic. I then toggled the priority to represent must-haves, should-haves, nice to have, etc. The priority of Each ticket would vary from sprint to sprint in line with an agile methodology ensuring each sprint is focused on the most critical tasks required to provide the necessary MVP.

## Sprint Notes

Below is a summary of learnings from each Sprint

### Sprint 1 Notes

![Sprint 1](/docs/agile/sprintscreenshots/sprint1.jpg)

The sprint's focus was to get the development environment step up and deployed to Heroku to test in production as early as possible.

* Due to the addition of AWS S3 bucket in this project, I allowed a little bit longer for a sprint than I did for my previous project. The allocated story points for each ticket indicate where I expect to spend more time on things due to lack of experience or previous issues when performing this aspect of the initial deployment of a project.
* This sprint began on 18/9/2022 at 02:00 and was due to finish at 21/09/2022 by 23:59.
* Finished well ahead of time, as I could complete all the tasks in less than 24 hours with no significant issues. It took a little longer than 24 hours to document the process in DEPLOYMENT.md; therefore, the higher story point values were warranted.

### Sprint 2 Notes

![Sprint 2](/docs/agile/sprintscreenshots/sprint2.JPG)

This sprint aimed to get the project's coding side up and running. I have decided to stick with one-week sprints as I did with my previous project. The planning aspect of this sprint has probably seen me overestimate the story points; however, because I took a break to focus on the new professional role, I wanted to ensure I had enough time to get back into the swing of things.

* This sprint began on 28/09/2022 at 22:00 and was due to finish at 5/10/2022 by 23:30.
* Finished a day late because it took a bit longer to arrange the styling as part of PV5-46. There were perhaps some additional parts to the styling I could have added. However, a sprint is supposed to be a set period that I had breached already, and the extra bits were not essential to meet the acceptance criteria or the tasks related to the ticket.
* I carried over PV5-10 to the next sprint as I could not complete it in time.

### Sprint 3 Notes

![Sprint 3](/docs/agile/sprintscreenshots/sprint3.JPG)

This sprint aims to get the products portion of the site up and running; I need to make the models to hold the product/category data, upload some products and then create the views to display the data to the user. This process will include creating the product admin page so I can manually add them to the site.

* This sprint began on 7/10/2022 at 17:45 and was due to finish at 15/10/2022 by 00:00.
* 55 story points are organized to be 60% must-haves, 20% nice to haves, and 20% should have.
* Finished a day late because I had issues with the polymorphic relationship between the AllProducts and subclass models. In the end, I had to go for a workaround due to time constraints. I will revisit this issue in the future.

### Sprint 4 Notes

![Sprint 4](/docs/agile/sprintscreenshots/sprint4.JPG)

The sprint aims at sorting products and starting the shopping cart.

* This sprint began on 20/10/2022 at 10:47 and was due to finish at 28/10/2022 by 00:00.
* 45 story points are organized to be 60% must-haves, 20% nice to haves, and 20% should have.
* Added a bug ticket [PVS-47](https://dnlbowers.atlassian.net/browse/PVS-47) part way through. Initially, I was going to leave for a later sprint; however, the fix became apparent as I was working on the product sorting, so I added it to this sprint.
* Sprint finished one day late again due to not having time to contribute on several sprint days. I could complete all the tasks in the sprint; however, technically, I should have concluded with one story remaining.
* Deciding to take a more relaxed approach for this project for my sprint ending dates. I will aim to finish the sprint on the due date; however, if I am unable to, I will not be too concerned as long as I have completed all the tasks in the sprint. That said, I would not drag out the sprint for more than one day(give or take an hour or two if working into the night) if I could not complete all the tasks.
* I realized several times during this sprint I need to focus on an MVP and get it working. Then, I can focus on the styling and other features at the end.

### Sprint 5 Notes

![Sprint 5](/docs/agile/sprintscreenshots/sprint5.JPG)

This spirit is aimed primarily at the checkout process and setting up the ability to make payments.

* This sprint began on 30/10/2022 at 12:40 and was due to finish at 07/11/2022 by 00:00.
* Since The first two stories are such large story point values and depend upon one being done before I can set up and test the other, I have now used Moscow by story points but rather by order of importance each task has. I shall use story points to organize by the moscow method once this sprint is complete.
* Realized I added [PVS-36](https://dnlbowers.atlassian.net/browse/PVS-36) to the sprint too early since this requires a user profile yet to be started.
* Finished a day late due to not having time to contribute on several sprint days and the stripe portion of the project taking longer than imagined. I could complete the stripe task in the sprint; however, technically, I should have concluded with it remaining and added it to the next sprint. I can do this due to being a team of one; however, in the real world, I would not be so flexible on this.

### Sprint 6 Notes

![Sprint 6](/docs/agile/sprintscreenshots/sprint6.JPG)

This sprint aims to get the user profile up and running and then add the ability to save the user's address from being reused.

* This sprint began on 09/11/2022 at 18:38 and was due to finish at 18/11/2022 by 00:00.
* Added [bug fix ticket PVS-53](https://dnlbowers.atlassian.net/browse/PVS-53) to this sprint mid-sprint as a quick fix, and I stumbled across it while working on the reviews.
* Added [bug fix ticket PVS-52](https://dnlbowers.atlassian.net/browse/PVS-52) to this sprint mid-sprint because it was blocking the completion of [PVS-20](https://dnlbowers.atlassian.net/browse/PVS-20).
* Changed review-related stories into their own [epic](https://dnlbowers.atlassian.net/browse/PVS-54) as I am planning to add edit and delete features to them.
* Finished sprint four days early. I overestimated the story points and could complete the tasks ahead of time. The earlier finish could also be attributed to having more time this week to spend on the project.

### Sprint 7 Notes

![Sprint 7](/docs/agile/sprintscreenshots/sprint7.JPG)

With the deadline fast approaching, this sprint aims to focus on the remaining features and bug fixes. I may have overstretched the number of stories; however, I have prioritized them and will focus on the most important ones first, the remaining will going in the next sprint. I may also have overstated my confidence in how quickly I will work some of these stories and give them a user point value that is too low. If required, I will see how I go and adjust in the newsprint.

* This sprint began on 13/11/2022 at 19:38 and is due to finish on 20/11/2022 by the same time.
* I decided that the stories relating to stock management for the admin on the front end are not essential to the project, as this is the purpose of the built-in admin panel. Instead, I will be looking to utilize best the built-in admin panel to make it as easy as possible for the admin to manage the site.
* I accidentally finished this sprint 19 hours early, thinking I was running late. I was left with three user stories, but all must-haves were concluded. I will not move the reaming three into the next sprint and start a new one.

### Sprint 8 Notes

![Sprint 8](/docs/agile/sprintscreenshots/sprint8.JPG)

This sprint is aimed at finishing the final features and marketing requirements. The sprint's last task is to tidy up and refactor without story points since this is a developer task and not a user story.

* This sprint began on 20/11/2022 at 16:00 and is due to finish at 28711/2022 by the same time.
* Added [bug fix ticket PVS-66](https://dnlbowers.atlassian.net/browse/PVS-66) to this sprint mid-sprint as a significant bug that needed to be resolved quickly.
* The sprint was concluded a day late, but in reality, the refactor task could have gone on for days

[Back to Readme](README.md)
