.. _Peer Assessments:

#########################
Open Response Assessments
#########################

*****************************************
Introduction to Open Response Assessments
*****************************************

Open response assessments allow instructors to assign questions that may not have definite answers. Students submit a response to the question, and then that student and the student's peers compare the response to a rubric that you create. Usually students will submit text responses. You can also allow your students to upload an image to accompany the text.

Open response assessments include peer assessments and self assessments. In peer assessments, students compare their peers' responses to a rubric that you create. In self assessments, students compare their own responses to the rubric.

For more information, see the following sections:

* :ref:`PA Elements`
* :ref:`PA Scoring`
* :ref:`PA Create a PA Assignment`
* :ref:`PA Accessing Assignment Information`

.. _PA Elements:

==========================================
Elements of an Open Response Assessment
==========================================

When you create an open response assessment assignment, you include several elements:

* The question, or prompt.
* The rubric.
* One or more assessment steps. Assignments can include a student training step, a peer assessment step, and a self assessment step.

.. note:: If you include a student training step, you must also add a peer assessment step. The student training step must be the first step.

For step-by-step instructions, see :ref:`PA Create a PA Assignment`.

************************
Question
************************

The **question** that you want your students to answer appears near the top of the page, followed by a field where the student enters a response. You can require your students to enter text as a response, or you can require your students to both enter text and upload an image. (All student responses must include text. You cannot require students to only upload an image.)



When you write your question, you can include helpful information for your students, such as what students can expect after they submit responses and the approximate number of words or sentences that a student's response should have. (A response cannot have more than 10,000 words.) 

For more information, see :ref:`PA Add Question`.

.. _PA Rubric:

************************
Rubric
************************

Your assignment must include a **rubric** that you design. The same rubric is used for peer and self assessments, and the rubric appears when students begin grading. Students compare their peers' responses to the rubric.

Rubrics are made of *criteria* and *options*.

* Each criterion has a *name*, a *prompt*, and one or more *options*. 

   * The name is a very short summary of the criterion, such as "Ideas" or "Content". Criterion names generally have just one word. Because the system uses criterion names for identification, **the name for each criterion must be unique.** Criterion names do not appear in the rubric that students see when they are completing peer assessments, but they do appear on the page that shows the student's final grade.

   .. you'll use criterion names when you create student training responses_

     .. image :: /Images/PA_CriterionName.png
        :alt: A final score page with call-outs for the criterion names

    * The prompt is a description of the criterion. 

* Each option has a *name*, an *explanation*, and a *point value*.

  .. image:: /Images/PA_Rubric_LMS.png
     :alt: Image of a rubric in the LMS with call-outs for the criterion prompt and option names, explanations, and points

  .. note:: You can also include criteria that do not have options, but that do include a field where students can enter feedback. For more information, see :ref:`TBD`.

You can see both criterion and option names when you access assignment information for an individual student. For more information, see :ref:`PA Accessing Assignment Information`.


.. image:: /Images/PA_Crit_Option_Names.png
   :width: 600
   :alt: Student-specific assignment information with call-outs for criterion and option names

Note that different criteria in the same assignment can have different numbers of options. For example, in the image above, the first criterion has three options and the second criterion has four options.

When you create your rubric, decide how many points each option will receive, and make sure that the explanation for each option is as specific as possible. For example, one criterion and set of options may resemble the following.

**Criterion**

Name: Origins

Prompt: Does this response explain the origins of the Hundred Years' War? (5 points possible)

**Options**

.. list-table::
   :widths: 8 20 50
   :stub-columns: 1
   :header-rows: 1

   * - Points
     - Name
     - Explanation
   * - 0
     - Not at all
     - This response does not address the origins of the Hundred Years' War.
   * - 1
     - Dynastic disagreement
     - This response alludes to a dynastic disagreement between England and France, but doesn't reference Edward III of England and Philip VI of France.
   * - 3
     - Edward and Philip
     - This response mentions the dynastic disagreement between Edward III and Philip VI, but doesn't address the role of Salic law.
   * - 5
     - Salic law
     - This response explains the way that Salic law contributed to the dynastic disagreement between Edward III and Philip VI, leading to the Hundred Years' War.

For more information about writing effective rubrics, see Heidi Goodrich Andrade's `Understanding Rubrics <http://learnweb.harvard.edu/alps/thinking/docs/rubricar.htm>`_.

For more information, see :ref:`PA Add Rubric`.

************************
Assessment Steps
************************

In your assignment, you'll also specify the **assessment steps**. You can set the assignment to include a student training step, a peer assessment step, and a self assessment step. 

You can see the type and order of the assessments when you look at the assignment. In the following example, after students submit a response, they complete a student training step ("Learn to Assess Responses"), complete peer assessments on other students' responses ("Assess Peers"), and then complete self assessments ("Assess Your Response").

.. image:: /Images/PA_AsmtWithResponse.png
  :alt: Image of peer assessment with assessment steps and status labeled
  :width: 600

.. note:: If you include a student training step, you must also include a peer assessment step. The student training step must come before the peer assessment step.

.. _PA Student Training Assessments:

==================
Student Training  
==================

When you create a peer assessment assignment, you can include one or more student training assessments to help students learn to perform their own assessments. A student training assessment contains one or more sample responses that you write, together with the scores that you would give the sample responses. Students review these responses and try to score them the way that you scored them.

.. note:: If you include a student training step, you must also include a peer assessment step. The student training step must come before the peer assessment step.

In a student training assessment, the **Learn to Assess Responses** step opens immediately after a student submits a response. The student sees one of the sample responses that you created, along with the rubric. The scores that you gave the response do not appear. The student also sees the number of sample responses that he or she will assess.

.. image:: Images/PA_TrainingAssessment.png
   :alt: Sample training response, unscored
   :width: 500

The student selects an option for each of the assignment's criteria, and then clicks **Compare your selections with the instructor's selections**. If all of the student's selections match the instructor's selections, the next sample response opens automatically.

If any of the student's selections differs from the instructor's selections, the student sees the response again, and the following message appears above the response:

.. code-block:: xml

  Learning to Assess Responses
  Your assessment differs from the instructor's assessment of this response. Review the
  response and consider why the instructor may have assessed it differently. Then, try 
  the assessment again.

For each of the criteria, the student sees one of the following two messages, depending on whether the student's selections matched those of the instructor:

.. code-block:: xml

  Selected Options Differ
  The option you selected is not the option that the instructor selected.

.. code-block:: xml

  Selected Options Agree
  The option you selected is the option that the instructor selected.

For example, the following student chose one correct option and one incorrect option.

.. image:: /Images/PA_TrainingAssessment_Scored.png
   :alt: Sample training response, scored
   :width: 500

The student continues to try scoring the sample response until the student's scoring for all criteria matches the instructor's scoring.

For more information, see :ref:`PA Add a Student Training Assessment`.


=====================
Peer Assessment
=====================

In the peer assessment step, students review other students' responses and select an option for each criterion in your rubric based on the response. Students can also provide text feedback, or comments, on the response. 

.. _Feedback Options:

Feedback Options
****************

By default, students see only a single comment field below the entire rubric. However, you can add a comment field to an individual criterion or to several individual criteria. The comment field can contain up to 300 characters.

The comment field appears below the options for the criterion. In the following image, the first criterion has a comment field, but the second does not.

.. image:: /Images/PA_CriterionAndOverallComments.png
   :alt: Rubric with comment fields under each criterion and under overall response
   :width: 600

Number of Responses and Assessments
************************************

When you specify a peer assessment step, you'll specify the **number of responses** each student has to assess and the **number of peer assessments** each response has to receive.

.. note:: Because some students may submit a response but not complete peer assessments, some responses may not receive the required number of assessments. To increase the chance that all responses will receive enough assessments, you must set the number of responses that students have to assess to be higher than the number of assessments that each response must undergo. For example, if you require each response to receive three assessments, you could require each student to assess five responses.

If all responses have received assessments, but some students haven't completed the required number of peer assessments, those students can assess responses that other students have already assessed. The student who submitted the response sees the additional peer assessments when he sees his score. However, the additional peer assessments do not count toward the score that the response receives.

Students can assess more than the required number of responses. After a student completes the peer assessment step, the step "collapses" so that just the **Assess Peers** heading is visible. 

.. image:: /Images/PA_PAHeadingCollapsed.png
   :width: 500
   :alt: The peer assessment step with just the heading visible

If the student clicks the **Assess Peers** heading, the step expands. The student can then click **Continue Assessing Peers**.

.. image:: /Images/PA_ContinueGrading.png
   :width: 500
   :alt: The peer assessment step expanded so that "Continue Assessing Peers" is visible


For more information, see :ref:`PA Specify Name and Assessment Types`.

.. _PA Scoring:

Peer Assessment Scoring
***********************

Peer assessments are scored by criteria. An individual criterion's score is the median of the scores that each peer assessor gave that criterion. For example, if the Ideas criterion in a peer assessment receives a 10 from one student, a 7 from a second student, and an 8 from a third student, the Ideas criterion's score is 8.

A student's final score for a peer assessment is the sum of the median scores for each individual criterion. 

For example, a response may receive the following scores from peer assessors:

.. list-table::
   :widths: 25 10 10 10 10
   :stub-columns: 1
   :header-rows: 1

   * - Criterion Name
     - Peer 1
     - Peer 2
     - Peer 3
     - Median
   * - Ideas (out of 10)
     - 10
     - 7
     - 8
     - **8**
   * - Content (out of 10)
     - 7
     - 9
     - 8
     - **8**
   * - Grammar (out of 5)
     - 4
     - 4
     - 5
     - **4**

To calculate the final score, add the median scores for each criterion:

  **Ideas median (8/10) + Content median (8/10) + Grammar median (4/5) = final score (20/25)**

Note, again, that final scores are calculated by criteria, not by individual assessor. Thus the response's score is not the median of the scores that each individual peer assessor gave the response.


=====================
Self Assessment
=====================

In self assessments, the student sees his response followed by your rubric. As with peer assessments, the student compares the rubric to his response and selects an option for each of the criteria. If you include both peer and self assessments, we recommend that you include the peer assessment before the self assessment. 


