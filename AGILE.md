# Agile Methodoglogy

## Overview

After using [JIRA](https://dnlbowers.atlassian.net/jira/software/projects/PVS/boards/5/roadmap) for [my last project](https://github.com/dnlbowers/jobs-a-gooden) to track my sprints, I decided to use it again for this project over git hub issues. JIRA has many more build in feature such as the analytics which assist me in the sprint planning and review process.

I split all user stories into several epics and linked each story, task, or bug fix ticket to the related epic. I then toggled the priority to represent must-haves, should-haves, nice to have, etc. Each tickets priority would vary from sprint to sprint in line with an agile methodology ensuring each sprint is focused on the most important tasks required to provide the necessary MVP.

## Sprint Notes

Below is a summary of learnings from each Sprint

### Sprint 1 Notes

![Sprint 1](/docs/agile/sprintscreenshots/sprint1.jpg)

The sprints focus was to get the development environment step up and deployed to Heroku to be able to test in production as early as possible.

* Due to the addition of AWS S3 bucket in this project I allowed a little bit longer for sprint than I did for myu previous project The allocated story points for each ticket indicate where I expect to have to spend more time on things due to lack of experience or previous issues when performing this aspect of the initial deployment of a project.
* This sprint began on 18/9/2022 at 02:00 and was due to finish at 21/09/2022 by 23:59.
* Finished well ahead of time as I was able to complete all the tasks in less than 24 hours with no major issues. I did however take a little bit longer than 24 hours to document the process in DEPLOYMENT.md and therefore the higher story point values were warranted.

### Sprint 2 Notes

![Sprint 2](/docs/agile/sprintscreenshots/sprint2.jpg)

This sprint was aimed at getting the coding side of the project up and running. I have decided to stick with one week sprints as I did with my previous project. The planning aspect of this sprint has probably seen me over estimate the story points however due to the fact that I took a break to focus on my new professional role I wanted to ensure I had enough time to get back into the swing of things.

* This sprint began on 28/09/2022 at 22:00 and was due to finish at 5/10/2022 by 23:30.
* Finished a day late because I took a bit long to arrange the styling as part of PV5-46. There were perhaps some additionally parts to the styling I could have added, however a sprint is supposed to be a set time period which I had breached already and the extra bits were not essential to meet the acceptance criteria or meet the tasks related to the ticket.
* I carried over PV5-10 to the next sprint as I was not able to complete it in time.

### Sprint 3 Notes

![Sprint 3](/docs/agile/sprintscreenshots/sprint3.jpg)

This sprint is aimed at getting the products portion of the site up and running, I need to make the models to hold the product/category data, upload some products and then create the views to display the data to the user. This process will include creating the admin page for products so I can manually add them to the site.

* This sprint began on 7/10/2022 at 17:45 and was due to finish at 15/10/2022 by 00:00.
* 55 story points in total organized to be 60% must haves, 20% nice to haves, and 20% should haves.
* Finished a day late because I was having issues with the polymorphic relationship between the AllProducts model and subclass models. in the end I had to go for a work around due to time constraints. and will revisit this issue in the future.

### Sprint 4 Notes

![Sprint 4](/docs/agile/sprintscreenshots/sprint4.jpg)

This sprint is aimed at sorting products and starting the shopping cart.

* This sprint began on 20/10/2022 at 10:47 and was due to finish at 28/10/2022 by 00:00.
* 45 story points in total organized to be 60% must haves, 20% nice to haves, and 20% should haves.
* Added a bug ticket [PVS-47](https://dnlbowers.atlassian.net/browse/PVS-47) part way through. Initially I was going to leave for a later sprint however the fix became apparent as I was working on the product sorting and therefore I added it to this sprint.
* Sprint finished on day late again due to not having time to contribute on several of the sprints days. I was able to complete all the tasks in the sprint however technically I should have concluded with one story remaining.
* Deciding to take a more relax approach for this project for my sprint ending dates. I will aim to finish the sprint on the due date however if I am unable to I will not be too concerned as long as I have completed all the tasks in the sprint. That said I will also not drag out the sprint for more than one day(give or take a hour or 2 if working into the night) if I am unable to complete all the tasks.
* I realized several time during this sprint I need to just focus on a MVP and get it working. Then at the end I can focus on the styling and other features.

### Sprint 5 Notes

![Sprint 5](/docs/agile/sprintscreenshots/sprint5.jpg)

This sprit is aimed primary at the check out process and setting up the ability to make payments.

* This sprint began on 30/10/2022 at 12:40 and was due to finish at 07/11/2022 by 00:00.
* Since The first two stories are such large stroy point values and are dependant upon one being done before I can realistically set up and test the other I have not used Moscow by story points but rather by the order of importance each task has. I shall return to using story points to organize by the moscow method once this sprint is complete.
* Realized I added [PVS-36](https://dnlbowers.atlassian.net/browse/PVS-36) to the sprint to early since this requires a user profile which is yet to be worked on.
* Finished a day late due to not having time to contribute on several of the sprints days and the stripe portion of the project taking longer than imagined. I was able to complete the stripe task in the sprint however technically I should have concluded with it remaining and added it to the next sprint. I am able to do this due to being a team of one, however in the real world I would not be so flexible on this.

### Sprint 6 Notes

![Sprint 6](/docs/agile/sprintscreenshots/sprint6.jpg)

This sprint is aimed at getting the user profile up and running and then adding the ability to save the users address to be reused.

* This sprint began on 09/11/2022 at 18:38 and was due to finish at 18/11/2022 by 00:00.
* Added [bug fix ticket PVS-53](https://dnlbowers.atlassian.net/browse/PVS-53) to this sprint mid sprint as it was a quick fix and I stumbled across it while working on the reviews.
* Added [bug fix ticket PVS-52](https://dnlbowers.atlassian.net/browse/PVS-52) to this sprint mid sprint because it was blocking the completion of [PVS-20](https://dnlbowers.atlassian.net/browse/PVS-20).
* Changed review related stories into their own [epic](https://dnlbowers.atlassian.net/browse/PVS-54) as I am planning to add edit and delete features to them.
* Finished sprint 4 days early. I over estimated the story points and was able to complete the tasks ahead if time. This could also be attributed to having more time this week to spend on the project.

### Sprint 7 Notes

![Sprint 7](/docs/agile/sprintscreenshots/sprint7.jpg)

With the deadline fast approaching, th aim for this sprint is to focus on the remaining features and bug fixes. I may have over stretched the amount of stories however I have prioritized them and will focus on the most important ones first. the remaining will going in the next sprint. I may also have over stated my confidence in how quickly I will work some of these stories and given them a user point value which is too low. I will have to see how I go and adjust in the new sprint if required.

* This sprint began on 13/11/2022 at 19:38 and is due to finish at 20/11/2022 by the same time.
* I decided that the stories relating to stock management for the admin on the front end are not essential to the project, as this is the purpose of the built in admin panel. instead I wil be looking to best utilize the built in admin panel to make it as easy as possible for the admin to manage the site.
* I accidentally finished this sprint 19 hours early thinking I was running late. I was left with three user stories, but all must haves were concluded. I will not move the reaming 3 into the next sprint and start a new.

### Sprint 8 Notes

![Sprint 8](/docs/agile/sprintscreenshots/sprint8.jpg)

This sprint is aimed at finishing the final features and marketing requirements. The last task in the sprint is the tidy up and refactor with out story points since this is a developer task and not a user story.

* This sprint began on 20/11/2022 at 16:00 and is due to finish at 28711/2022 by the same time.
* Added [bug fix ticket PVS-66](https://dnlbowers.atlassian.net/browse/PVS-66) to this sprint mid sprint as it was major bug and needed to be resolved quickly.
