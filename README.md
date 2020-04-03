Fabulous Recommendations (FabRec)
========================================================
By Jina Lo, Nayeong Kim, Rose Kong, Shannie Cheng
-------------------------------------------------

Fabrec is a fashion recommendation service that crowdsources outfit recommendations using Amazon Mechanical Turk. We recommend complementary fashion items based on the clothing item our customers own. For example, a customer want to find a skirt that would goes well with the top she owns. She would upload the picture of her top and Fabrec would give her some options of skirts with a link of each item as recommendations.

The final report for this project can be viewed in _report.pdf_ and video link to this project is https://vimeo.com/334820841.  


Data Collection
========================

Data Collection consists of parts: color matching task and style matching task. This module is intended to get all the good color matches and style matches using crowdsourcing platform, Amazon Mechanical Turk. The data collected in this module would be used later to give recommendations to Fabrec customers.


Color Matching
--------------

Color matching uses crowdsourcng website Amazon Mechanical Turk to collect possible outfit color matchings. Specifically, we post Human Intelligence Task (HIT) with palette of solid colors and crowdworkers would pick 2 colors, which represents the 2 colors of clothes in an outfit, of their preference. Their input would be taken into account to later help Fabrec customers get recommendations based on the color of clothes they have inputted.

For example, our HIT would ask crowdworkers to choose 2 colors for the dress and shoes outfit. A crowdworker may give us her preference of a blue dress and black shoes, where her color preference of blue and black matching would be recorded in our dataset. Later when a Fabrec user uploaded a blue dress to get recommendations, we would fetch the blue and black matching in our dataset and crowdsource a pair of black shows for our customer as recommendations.


Style Matching
--------------

Style matching uses Amazon Mechanical Turk to collect different matching of outfit styles. Given a visual glossary of top/pants/skirts/dress/shoes styles, crowdworkers are asked to select style of their choice to make an outfit. Specifically, our HIT consists of three kinds of style matching. A crowdworker would be asked to find a top + pants + shows, top + skirts + shoes, or dress + shows outfit style, where their input would be recorded and later used in Fabrec recommendation generation step.

For example, a crowdworker is asked to input a style of top and a style of pants. Upon receiving his input of a crewneck shirt with a 5-pocket jean, we record his preference in our dataset. When a user upload red crewneck shirt on Fabrec's website, we would retrieve both the crewneck shirt and 5-pocket jean matching and a red and blue outfit matching from our dataset. Our user would then receive a blue 5-pocket jean item as recommendations.


User Interface
========================

Fabrec is an online fashion recommendation website, where based on a user's input of a clothing image, we would offer our user top 3 ranked item that would fit well with their input clothes.


User Input Module
-----------------

This module is the first step for Fabrec users to get recommendations, where Fabrec users are asked to upload an image of a piece of clothes such as a top, a pair of pants, a skirt, or a pair of shoes.


Color-Style-Matching Module
---------------------------

Based on the input from Fabrec user, we are going to crowdsource the task of getting recommendation for such piece of clothes using Amazon Mechanical Turk. In this HIT, we are giving crowdworkers the user input, recommended color matching and style matching from the Data Collection step. Crowdworkers would give us specific link of a piece of clothes, with reference of the recommended color and style matching, that they think would be a good match to the input


Aggregation Module
------------------

This is the aggregation module where we would aggregate all the links that crowdworkers inputted and process all the links to prepare for the quality control module.


Ranking and Quality Control Module
----------------------------------

This module would include the quality control of the content as well as ranking of the clothes recommendations. We would create another HIT on Amazon Mechanical Turk where crowdworkers are provided with links inputted from the Color-Style-Matching Module. Crowdworkers would then check the content each link is directed to and remove any out-of-category links. Crowdworkers provide their top 3 clothing link.

Quality of the recommendations is gauranteed by asking crowdworkers to remove the out-of-category links and provide top 3 ranking, which would ensure that crowdworkers have looked at the content each link is directed to.


Recommendation Output
---------------------

The aggregated top ranked clothing links would then be recommendations we give to Fabrec users.


Business Model
========================

In order to maintain a consistently updating website, we would strongly recommend Fabrec customers to provide recommendations as well getting recommendations. Therefore, we kindly ask Fabrec customers to submit 5 HITs before getting their recommendations.
