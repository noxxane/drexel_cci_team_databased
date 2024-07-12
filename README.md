# Team DataBASED - Improving Political Participation Amongst Young Teens
Repo for Team DataBASED as part of the 2024 Drexel CCI camp. Our project, Teenformation intends to improve participation in the political process amongst young people by exposing and elucidating political inefficiencies and disclosing opportunities for participation for those below voting age. Teenformation offers a data-based, unbiased approach to politics with no party affiliation. Our sole goal is to offer a view into politics for those denied partcipiation and to improve systemic inefficiencies that contribute to political disengagement.

The only feature currently fully implemented is a scraper for the house.gov zip code to rep thingamajing written in Python. The Python program creates a JSON (or CSV, but nobody likes this one) file which is then fetched by the website and parsed from there. The user's zip code is just taken from an input element and it can be shown to them from there.

## TODO (according to Cole)
- State to Senators.
    - Could be implemented in basically the same way as the House one is just without the need for any scraping or other complicated stuff. There might already be a dataset for this but I wouldn't mind programming something to automate it.
- Something with the 2023 Philadelphia mayoral election data.
- Voter participation in United States elections over time.
    - Early elections had extremely low participation which slowly rose over time.
    - However, there are a number of spikes in election participation (assumedly), including:
        - The passage of the 13th Amendment.
        - The passage of the 19th Amendment.
    - Additionally, participation generally falls during periods of war or political dominance.
        - For instance, in the 1812 election, Democratic-Republican James Madison (the incumbent) received 52.3% of the votes with a 40.4% turnout. This was the second-to-last election wherein the Federalists ran a presidential candidate, beginning a period of Democratic-Republican domination. This domination was reflected by turnout numbers in the following elections. In the 1816 presidential election, Democratic-Republican James Monroe won 72.9% of the vote with a *16.9%* turnout. The turnout only recovered to 1812 levels in 1828 presidential election, which marked the end of the First Party System and the beginning of the Second Party System. In other words, during the period of Democratic-Republican dominance, turnout plummeted, not recovering until the end of that dominance. Andrew Jackson won only 55.5% of the vote in 1828; by comparison, no political party so much as *ran* a presidential candidate against James Monroe in 1820.
    - Participation also falls when voters feel they have less agency, particularly when an incumbent is running for reelection. However, this pattern reverses with unpopular presidents, like Herbert Hoover or Donald Trump.
        - In the 2008 presidential election, Barack Obama received 52.9% of the vote with a 61.6% turnout. In the 2012 presidential election, Obama received 51.1% of the vote with a turnout of 58.6%, representing a 3 percentage point drop. It is worthy of note that from September 11 through November 6, Barack Obama was only below Mitt Romney, his Republican opponent, in nationwide opinion polling for tmost of the month of October. Even then, he was only trailing Romney by a few percentage points. He rebounded at the end of October and outperformed his polling by two points, although Romey also improved over the polling by one point.
        - An example of the opposite of 2012 is the 2020 presidential election, when Joe Biden won by 51.3% with a 66.6% turnout rate, representing a 6.5 percentage point improvement over 2016. From October 1 to November 3, Joe Biden only polled lower than Donald Trump in two polls, both of which could be flipped either way accounting for error. In polls administered a day prior to the November 3 election, Biden was favored by as much as *8 points*. From 2017 to 2021, Donald Trump's national approval rating never reached 50%. Indeed, his disaprooval rating reached its lowest, roughly 60%, around Joe Biden's inauguration and the January 6 attack.
- Data from Germany, New Zealand, Alaska, and New York City pertaining to what happens when electoral systems more proportional that first-past-the-post are used.
    - German federal election turnout has never fallen below 70.8% percent, which occurred in 2009 at the height of the CDU/CSU's dominance. This election was the second in which Angela Merkel ran as a candidate for Bundeskanzler. This relatively consistent high-turnout can likely be ascribed to Germany's electoral system, a mixed-member proportional representation political system. Under this system, a voter casts two votes: one for a constituency representative and one for a party. The constituency candidate is elected to that constituency if they receive a plurality of the vote, while the party vote contributes to a party list. The voter's party vote goes to a party list, from whence candidates are elected based on the percentage of nationwide or region-wide votes that each party received. This ensures proportionality; even if a party wins more constituency seats than another, they will both receive around the same number of seats if their vote percentage is similar.
    - In New Zealand, after the adoption of the MMP system (the same used in Germany), election turnout rose by 5.46% to reach a whopping 88.28%. Voter turnout has fallen slightly since, but has never dropped below 76.98%, as took place in the 2002 general election. However, this drop in turnout can also be explained by the weakness and poor performance of the National Party, the main opposition to the victorious Labor Party, whose electorate and party votes both climbed; by comparison, the National Party's electorate vote dropped by 1.38% and its party vote by 9.57%. Additionally, the Labor Party was the governing party at the time, having led the National Party in 1999 by roughly 10 percentage points in both electorate and party votes.
    - In 2020, Alaska Measure 2 was adopted by voters in Alaska, establishing a non-partisan blanket primary using ranked-choice voting in lieu of the regular partisan primary system. Under the new RCV system, Mary Peltola was elected to the Alaska at-large congressional district in a 2022 special election. Peltola's election was an upset, being the first Democrat to win a statewide election in Alaska since 2008. In the ensuing 2022 regular elction, contrary to the usual incumbent drop, 70000 or so more voters voted for the advancing candidates in the primary election. Peltola also improved on her performance in the previous election, receiving 50000 or so more first round votes and 40000 or so more maximum round votes.
    - In 2019, Ballot Question #1 was passed in New York City, which amended the City Charter, putting in place ranked-choice voting. The effect that this adoption had is most visible when comparing the 2021 and 2013 Democratic primary (2017 is not used as Bill de Blasio, victor in 2013, was an incument then). In 2013, 691801 voters participated in the Democratic primary, representing a turnout of 23.67%. In 2021, the *top 4 round 1 candidates*outperformed the *total 2013* primary turnout by 98322 votes. When accounting for all round 1 candidates, 250230 more voters participated in the 2021 primary than the 2013 primary.
    - Proportionality is innately tied to voter participation. In the United Kingdom, where voter participation has undergone a continuous drop since its height in 1950, when 83.9% of voters participated. The lowest ever recorded was 1918's dismal 57.2%, which was almost matched by the recent 2024 general election, in which 60% of voters participated. The United Kingdom's first-past-the-post parliamentary system is oftentimes among the most disproportionate in the world. In the most recent election, despite only receiving 33.7% of the popular vote, the Labor Party won 412 seats in Parliament, representing 63.2% of the seats in Parliament. Comparatively, the far-right Reform Party received 4,117,221 votes (roughly 600,000 more votes and 2.1 more percent than the Liberal Democrats, who won 72 seats) but only won five seats --- 0.8% of Parliament. In summary, Labor received close to *double* the representation in Parliament as received in the popular vote while the Reform Party saw nearly 1/20 of their vote share translated into Parliament seats. Prior elections were similarly disproportionate. In the 2015 general election, Ed Miliband's Labor Party received 30.4 of the popular vote, a 1.5 percentage point swing upward from the previous election; however, this (somehow) translated into a seat change of *-26.* The SNP, whose support was nonexistent save for in Scotland, where it was dominant, received only 4.7% of the nationwide vote but won nearly double that in Parliament seats. The United Kingdom's disproportionality is most directly revealed when looking at third parties like the Greens and the far-right UKIP (whose leader Nigel Farage later joined the Brexit Party, which became the Reform Party). In the 2015 general election, UKIP placed *third*, above the Liberal Democrats, with 12.6% of the popular vote. In return, it received *a single* seat in parliament. Likewise, the Greek Party received 3.8% of the popular vote but only received a single seat in Parliament. As mentioned previously, the SNP won 56 seats in this election with 1,454,436 votes; the Greens received 1,111,603. One SNP seat represents 25972 voters when considered nationwide; one Green seat represents *the totality of the Green voterbase*. *One SNP voter is worth 42.8 Green voters.*
- Gerrymandering
    - Examples of gerrymandered districts and data from them.
        - Maybe model how those elections could turn out if they were not gerrymandered.
    - First-past-the-post is particularly vulnerable to gerrymandering, and proportional representation is far less vulnerable thereto.
- Webdesign Stuff (not for me but I figure that sometimes I think of things that make vague senes so what the flippity flop it's here anyway)
    - Inspiration
        - [Molly White](https://blog.mollywhite.net)
            - More than anything else (although the font and margins are still definitely inspiration), I think that Molly's footnotes are something that we could definitely use. The way I think about it, a lot of our site is going to be focused on stuff that would definitely be cited in a universe which makes sense, and footnotes are better than any other style of citation in my opinion.
        - [Gwern](https://gwern.net)
            - Couldn't so much as imagine implementing all the stuff that Gwern has, especially the Wikipedia-like popouts. I do think his typography and the way that his articles are formatted are nice though. They're basically shown like a journal article just in a webpage, which I think is pretty good. Also footnotes.

## Further Information
### Published Research on Voting
- [Voting Correctly](https://www.researchgate.net/profile/David-Redlawsk/publication/265424751_Voting_Correctly/links/57f7dba508ae91deaa606685/Voting-Correctly.pdf)
- [Condorcet's Theory of Voting](http://faculty.econ.ucsb.edu/~tedb/Courses/UCSBpf/readings/PeytonYoungCondorcet.pdf)
- [Values and Voting](https://d1wqtxts1xzle7.cloudfront.net/49836971/0162-895x.0009020161024-6324-16dglqt-libre.pdf?1477326781=&response-content-disposition=inline%3B+filename%3DValues_and_Voting.pdf&Expires=1720756414&Signature=BQjceygF2HPOJSapGvJierYVqeXho~0NSu~mzI63kGZhuqu~FJ0aV6EM~Fbu2ZNwPBBpDxkgSbQzDvxvmoZS5UfdwJH0~b19F-JQZiccaDBnMq-q6Cm9Al0GUR9o90auLV~SP3dxBp5PbLl7WN8dCbwRoM7KBaZF~TMMcvMCRXu7vAP0eew8WWnPGHccNiilxhsA~hj5JzOdwLpoMonV3yujxTXXrnHBCO5WyYgNgZjh4STSk1Mn6eBZ27lFOD76dPY2jKvrtbfTJSCj4g8ITitGdrdc5RR6XpO6ziVV8UrYs1ayvLcEsd6QIjw84QmYGku5DqvLnxXED3T0Q-ap1w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
- [Problems of Majority Voting](https://cooperative-individualism.org/tullock-gordon_the-problems-of-majority-voting-1959-dec.pdf)
- [Optimal Voting Rules](https://pubs.aeaweb.org/doi/pdf/10.1257/jep.9.1.51)
- [Disapproval Voting: a characterization](https://gredos.usal.es/bitstream/handle/10366/127275/Disapproval.pdf?sequence=1)
- [A Theory of Voting Equilibria](https://www.econstor.eu/bitstream/10419/221141/1/cmsems-dp0782.pdf)
- [Manipulating of Voting Schemes: A General Result](https://d1wqtxts1xzle7.cloudfront.net/101646701/4e0b06cb0c26d44f0fc86fa0a1ecfc4d13b1-libre.pdf?1682820461=&response-content-disposition=inline%3B+filename%3DManipulation_of_Voting_Schemes_A_General.pdf&Expires=1720756452&Signature=au~XPF1FSum3gH4Xtt2KK6ZC5spKNN0~YXkyF925hVEe119Q4Oz50ojrCOtYifLAZN166LvfYtJx-bvWWAXr5AZ27a3lDLHX5vbiLyR-4Cv6972wqa1qHnEFaKrrcE9dm6EwBZpiy-sj87LP-5JLTmQYGgopzWlfLX7VwWeL6gAh4v1fIv2yItkigvns5sQPdh1HqkZi6E6dIxCPvZus6ycLQ-VYIRv9Y4DnExYAseB8GFGgw6bH1z-9QkkUUrJsMzFwjcgIu7oydsZifDCgAnSvDeNfDlKhgyD~poR8QY975gDHWn34aC8FhroXq0ZMuDM2LGs85hSP8BOSVbSLAw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
### Published Research on Political Disengagement
- [Emerging Adult Civic and Political Disengagement: A Longitudinal Analysis of Lack of Involvement with Politics](https://youthandreligion.nd.edu/assets/124526/psnell_emerging_adult_civic_disengagement.pdf)
- [Some Elements of an Interactionist Approach to Political Disengagement](https://serval.unil.ch/resource/serval:BIB_901FDF515554.P001/REF.pdf)
- [Political Disengagement Among Youth: A Comparison Between 2011 and 2020](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.809432/full)
- [Social Capital and Political Participation:]
