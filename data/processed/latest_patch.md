## 
> It’s our first main patch for Enchanted Wilds, but if you’ve missed the several mid-patch updates for 18.1, you can always catch up on those changes [here](https://teamfighttactics.leagueoflegends.com/en-us/news/game-updates/teamfight-tactics-patch-18-1/); there were a lot. As for this patch, our focus is on continuing to squash bugs, with more bugfixes and performance improvements planned for the next few patches. On the gameplay side, we’re enabling comps that haven’t had the chance to shine under the canopy of reroll and Ahri, while also making some small adjustments to the economy to support leveling to 8, 9, and 10 via direct cost reductions per level and cheaper combat Wisps throughout the game. As they say, more gold in the bank, more chances to miss in your rolldown.
![](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/324f7ff1edf0e0864b56f4068281aafdbb9af5f8-300x300.png) Rodger "Riot Prism" Caudill
![](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/f6bf389636317d0e33ef7ab51c72928eda133f83-300x300.png) Katie "Riot Ukime" Guo
## MID-PATCH UPDATE
#### SEPTEMBER 14
> 18.2 set out to enable fast 9 strategies amidst a reroll-heavy meta of 18.1, but through more econ via cheaper Wisps, lower leveling costs, and powerful buffs, Legendary-soup variations quickly shifted what S-tier stands for.
---
#### SYSTEMS
> Our 18.2 changes to XP reduced the cost of going to Level 10 by 12 gold—that’s a lot in the world of TFT, especially when you’re saving anywhere from 5-15 gold on cheaper Wisps. We’re not doing a total revert of the XP changes here, as we’re keeping it cheaper to go from Level 7 to 8 by 4 XP/gold, but 9 and 10 are getting their changes reverted.
* XP From Level 8-9: 64 ⇒ 68
* XP From Level 9-10: 64 ⇒ 68
---
#### AUGMENTS
> As expected, Expected Unexpectedness has been re-enabled, but a newly unexpected bug has had us pull Nesting Dolls temporarily.
* Expected Unexpectedness Re-enabled
* Nesting Dolls Disabled due to a bug
---
#### UNITS
> Camille has found her place as a powerful reroll carry in Solar/Ravager boards even in a meta that leans towards fast 9. Since we’re nerfing all our Level 9/10 comps and a few more pricey units, we’re pre-emptively delivering a weightier nerf for our best performing reroll comps.  
>   
> LeBlanc is still being used as more of a reroll printer than a unit that sticks around on end-game boards. We’re lowering her base chance to print at three-stars, but as an itemized carry she should still be pretty consistent as a champ printer since the bonus chance via takedowns is unchanged.  
>   
> Fixed some odd bugs that had Brambleback’s Armor Ignore being higher than intended in cases where he was not building AP and lowering when he built AP. Brambleback will be stronger with things like Titan’s Resolve, Bloodthirster, Edge of Night—all of which grant AP, but he will be slightly weaker without these Items or other sources of AP.  
>   
> Even before the rise of fast 9, Draven had some powerful Bounties that leveraged easier tasks for substantial rewards. Draven is a reward unto himself (just like you), so we’re trimming the easier rewards or just making them slightly harder (I’m sure he can handle it).  
>   
> With Level 8 cheaper, players are getting Maokai online much easier (same applies to Draven) and are able to stack up a lot more HP. We love the Old Growth, giant HP bar fantasy, so our nerfs are targeted at his ability to repeatedly cast and heal up over the course of a fight.
* Camille Ability Damage: 160/240/410/700 AD ⇒ 150/225/375/640 AD
* Leblanc Clone Chance: 10/15/40% ⇒ 10/15/30%
* Teemo Small Shroom Damage: 60/90/135 AP ⇒ 55/82/130 AP
* Brambleback: Fixed a bug where his baseline Armor Ignore was higher than intended.
* Brambleback: Fixed a bug where his Armor Ignore would decrease with increasing Ability Power.
* Brambleback Armor Ignore: 15 + 30% AP ⇒ 20 + 25% AP
* Ashe Trail Duration: 4s ⇒ 3s
* Ashe DoT Base Damage Per Second (AD): 5/8 AD ⇒ 9/14 AD
* Draven Bounty Hunter:
  + Casts for 4-costs: 5 ⇒ 6
  + Reward for 8 Casts: 10 Rerolls ⇒ 6 Rerolls
  + Attack for 5-cost: 50 ⇒ 60
  + Damage for 7 Gold: 8,000 ⇒ 10,000
  + Kills for 12 Gold: 6 ⇒ 8
* Maokai Mana: 30/90 ⇒ 30/100
---
#### WISPS
> Last second Polymorphs are cool, but they’re rarely a good idea as your 3 cost Vi becomes a frontline Aphelios without the time to reposition.
* Polymorph: All Polymorph Wisps can only be seen as the 1st Wisp of each Planning Phase.
---
#### BUG FIXES
* Fixed a bug where Auto Attack projectiles could get stuck on a dashing champion and deal much more damage than intended.
* Fixed a bug where Krug and Yorick would not spawn their summons when sacrificed by the Blackthorn Hex.
* Fixed a bug where Thief’s Gloves would offer different items when re-equipped to another champion during the same round.
---
#### PERFORMANCE/STABILITY BUG FIXES
* Fixed an issue where version mismatch would result in players being stuck on a spinner instead of being notified of a version mismatch with a popup modal
* Fixed a crash issue found on PC related to item subsystems
* Fixed an infinite loading screen issue that occurred when using some VPNS
* Fixed an issue on Tablet where Stylus taps were not being registered
* Fixed performance issues with the following cosmetics/VFX: Twilight Forest Arena, Unbound Katarina, Blaze Wisp
## 18.2 PERFORMANCE/STABILITY IMPROVEMENTS
> We usually don’t get this technical in our Patch Notes, but alongside all the more visible gameplay bugfixes like Sentinel targeting the wrong line of enemies or Kennen’s ability losing visuals, we’ve got some even more invisible improvements that’ll affect performance and stability across both PC and Mobile.
---
* Niagara/VFX performance and leak prevention:Our particle flushing tool has been improved to help get rid of particles no longer in play, opening up room for high performance even as fights get more complex and Tactician HP gets lower. Our fix here focuses on solving leaks and detecting more, with a few of note coming from persistence VFX like waterfalls, Tactician effects and gameplay abilities.
* Engine Load/Start-up: Improved server load times through asset loading and nav-mesh tile processing.
* Engine Load/Start-up: Optimized asset registry to avoid slow load times on startup
* Engine Load/Start-up: Optimize loyalty asset-registry queries and parallelize asset-registry rebuilds.
* Frame-time improvements: Pipeline State Object precache updates; preloading GPU shader/rendering pipeline configs ahead of time to avoid frame stutters when they’re first used
* Frame-time improvements: Skeletal-mesh tick sorting optimized to reduce dependencies (threads waiting on each other before updating)
* Engine Load/Start-up: Improved asset preloading and make CEF load on demand to speed up boot time
* Memory, mobile, rendering, and thermal performance: Dynamically unload arena intro sublevels.
* Memory, mobile, rendering, and thermal performance: Enable the RHI thread on iOS for rendering hardware interface calls, improving parallelism
* Memory, mobile, rendering, and thermal performance: Dynamically loading texture detail based on need; disabling it on high-VRAM PCs since they can just hold everything in memory.
* Memory, mobile, rendering, and thermal performance: Improve Android thermal-throttling, making smarter throttling decisions around maintaining device temperature.
* Memory, mobile, rendering, and thermal performance: Fixed some devices OOM (Out of Memory, not to be confused with out of mana), watchdog termination (when your phone kills the app to save memory, a phone’s mana), and recurring crashes without crash reports
* Memory, mobile, rendering, and thermal performance: Add memory usage tracing and measure practical memory availability on mobile.
* Runtime stability and performance hygiene: Prevent crashes during pooled-actor cleanup and reuse. Now we can properly reuse assets without destroying/recreating them as the circle of life intends
* Runtime stability and performance hygiene: Fix phase-restricted gameplay effects that linger beyond their intended phase.
* Crash diagnostics, and crash fixes: Added a series of improvements to prevent crashes around 4 of our highest volume crashes.
## PATCH HIGHLIGHTS
[![](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/111021b211b02a3ee659c69de350c66707f002d8-1920x1080.jpg)](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/111021b211b02a3ee659c69de350c66707f002d8-1920x1080.jpg)
---
[![](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/72ed5fbf4182d25e1519d31bdaa6ca541db65593-2250x2813.png)](https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/72ed5fbf4182d25e1519d31bdaa6ca541db65593-2250x2813.png)
## COSMETICS AVAILABILITY
> We have a lot of work left to go on converting cosmetics over to Unreal, and we want to assure everyone that **every** cosmetic in the catalog will be making its way back to TFT. We see you, Sugarcone Furyhorn enjoyers. Along with bugfixes and performance improvements, it’s a top priority to get converted cosmetics back into the game ASAP.  
>   
> As of Patch 18.2, we’re expanding access to **all** available cosmetics released prior to Enchanted Wilds for players who own any cosmetic at a given rarity tier (i.e. if you own a Mythic Chibi, you get access to all tacticians Mythic rarity and below). When we’re further along with re-adding cosmetics, we’ll get back to business as usual.  
>   
> Moving forward, every set of patch notes will also include a section going over cosmetics converted in the current patch, as well as what’s up next. Patch 18.2 contains another batch of cosmetics, with more planned for 18.3 and beyond. This work has taken longer than we expected, and we know you’re waiting on both your cosmetics and more information. We want to make sure every cosmetic meets our quality bar before bringing it back, along with ensuring they don’t introduce new bugs or performance issues to TFT, and we appreciate your patience as we work through the catalog.  
>   
> **For a full list of the Cosmetics being converted for Patch 18.2 and what’s coming up next, click** [**here**](#patch-cosmetics-converted-in-patch-18.2) **or scroll to the bottom of these notes.** This next bit is a little bit in the weeds, but for players interested in more technical details and how we’re prioritizing, read on.  
>   
> We’re working through the catalog based around a few key factors:
>
> * We’re prioritizing the most popular cosmetics first, the ones most players were actively using before our engine migration.
> * We’re also prioritizing the highest-rarity cosmetics that players have invested in. These are primarily Legendary, Mythic, and Prestige rarities.
> * We’re also balancing that against cosmetics that can be delivered most quickly to successfully migrate at our target quality bar without negatively affecting gameplay performance. Some cosmetics just take longer to optimize than others, and they each go through quite a few steps before implementation to make sure they aren’t going to cause additional bugs, crashes, or performance issues.
> * As we get through more patches, we’re expecting to accelerate the rate that cosmetics are being converted, but we have a lot to work through, so we’ll be continuing to bring over more content throughout the course of Enchanted Wilds.
> * By our final patches where we’ll be converting cosmetics, we’ll be mostly bringing over content with the lowest population of players who actively use them, but they’ll all make their way over eventually - we care about the Matcha Cuppy players out there.
> * We continue to learn along the way, and what we learn may change the list of cosmetics coming in each patch, but we’ll continue to provide as much clarity as we can when that happens, and keep everyone updated on what’s coming next along the way.
## SYSTEMS
#### XP PER LEVEL
> Coming off of an inflationary set mechanics (God offerings in Space Gods), getting to late levels in the game has been hard. Getting 4 gold back on levels and having Wisps be slightly cheaper should help ease you into pressing that XP button more often, cause we all know, you can miss a roll down, but you can’t miss the XP button (I hope).
* Level 7 to Level 8: 60 ⇒ 56
* Level 8 to Level 9: 68 ⇒ 64
* Level 9 to Level 10: 68 ⇒ 64
## LARGE CHANGES
> Large, like a lifetime.
---
#### TRAITS
> Blackthorn is a trait that only sees play as a (2) piece, and it’s almost exclusively used to sacrifice a tank (cries for Kobuko). We’re giving it some bigger buffs at (4) and (6), while increasing the rewards for sacrificing the occasional caster and AD carry.  
>   
> Coven is getting Caitlyn cashouts, so if you are playing Caitlyn reroll, you can hope to get a couple copies off of a lower breakpoint cashout. Other cashouts are getting a bit more exciting, more varied, and more powerful for the harder to hit ones.  
>   
> Fae (4) will be a bit easier to hit the Golden Pixies, especially early on, where the mid-game infusion of gold feels a bit more magical.  
>   
> Hunter has a cool fantasy of focusing down a target to take it out, but 4 seconds is an eternity in TFT, so we’re lowering that damage amp bonus to 3 seconds, a much more realistic amount of time. Expect this trait to feel a lot better in taking down tanks.  
>   
> Solar is very strong late game, with one of the highest first place rates, but it’s pretty weak early, making it far riskier than we intended. We’re giving the trait a small early game buff, but overall this is a nerf to Solar.
* Blackthorn:
  + Health: 175/300/550 ⇒ 175/350/600
  + Tank Sacrifice Resists: 15 ⇒ 12
  + AD Sacrifice Base AS: 12% ⇒ 14%
  + AP Sacrifice Base Mana Regen: 1.7 ⇒ 2
* 130 Essence Coven Cashouts Added:
  + 2\* Caitlyn + 1 Component + 3g
* 185 Essence Coven Cashouts Added:
  + 1 Completed Anvil + 2\* Caitlyn + 2\* Camille
  + 1 Completed Anvil + 8g ⇒ 1 Completed Anvil + 10g
* 250 Essence Coven Cashouts:
  + 2 Completed Item Anvils + 12g ⇒ 2 Completed Item Anvils + 20g
  + 2\* Morgana + Lucky Item Chest + Component Anvil ⇒ 2\* Morgana + Lucky Item Chest + Random Completed Item + 3g
  + 2x Lucky Item Chest + 6g ⇒ 2x Lucky Item Chest + 18g
  + Lucky Item Chest + 2x Component Anvil + Coven Lux + 5g ⇒ Lucky Item Chest + 2x Component Anvil + Coven Lux + 18g
  + 1x Artifact Anvil + 1x Completed Anvil + 5g ⇒ 1x Artifact Anvil + 1x Completed Anvil + 18g
* 365 Essence oven Cashouts:
  + All rewards grant an additional 12 gold.
  + 2x Radiant TG + 20g ⇒ 2x Radiant TG + 2\* Kennen + 15g
* Fae Golden Pixie Breakpoints:
  + 1st: 200,000 ⇒ 170,000
  + 2nd: 250,000 ⇒ 200,000
  + 3rd: 330,000 ⇒ 300,000
  + 4th: 420,000 ⇒ 400,000
  + 5th: 510,000 ⇒ 500,000
  + 6th: 610,000 ⇒ 600,000
* Hunter Targeting Duration for Damage Amp: 4 seconds ⇒ 3 seconds
* Inferno Burn: 1/1/3/3.5% ⇒ 1/1/3.5/4.5%
* Rapidfire AS Per Attack: 3/5/9/15% ⇒ 3/5/8/12%
* Solar:
  + Initial Bonus Magic Damage: 7% ⇒ 8%
  + Bonus Increase per 3-star: 1.5% ⇒ 1%
  + Three 3-star Bonus Attack Speed: 18% ⇒ 15%
  + Three 3-star Armor and Magic Resist: 15 ⇒ 12
---
#### UNITS: TIER 1
> Ravagers are alright as an early game opener, but they fall off harder than any other comp. We’re shipping quite a lot of buffs to the Ravagers to hopefully carve out a spot for these units to be solid reroll carries into the mid-game.  
>   
> Alongside our Solar nerf, we’re giving a compensation buff to Leona, the trait’s worst unit and our worst performing 1-cost tank. A buff to her Mana and decaying resists should brighten up her day.  
>   
> Veigar’s tooltip was bugged to not accurately reflect the actual AP gain he was getting—you could say it left him a little short. But much like real life, being short didn’t hinder our short-king, as he was still getting the proper amount of AP from his stacks behind the scenes.
* Akali AD Form Mana: 0/30 ⇒ 0/25
* Leona Mana: 40/100 ⇒ 30/90
* Leona Decaying Resists: 60/70/80/100 ⇒ 60/80/100/130
* Varus Ability Damage: 385/580/925/1530 AD ⇒ 415/625/1000/1700 AD
* Veigar Bugfix: Veigar’s AP per kill in his tooltip now matches the actual AP Gained. Visual AP Per Kill: 1.5% > 3% (functionally no change)
---
#### UNITS: TIER 2
> We’re moving a bit of LeBlanc’s passive printing power into her Ability damage, so she can be used as a more reliable item-holder as well as a cloning machine.  
>   
> As with our buff to Leona, we’re able to buff Kayle more now that Solar’s late-game potential is in check.  
>   
> 5 AD may be an ancient meme of balancing, but it’s a pretty significant buff for Warwick who attacks A LOT!
* LeBlanc Ability Damage: 250/375/565/955 AP ⇒ 260/390/615/1045 AP
* LeBlanc AoE Damage: 85/130/190/325 AP ⇒ 100/150/230 AP
* Kayle Magic Damage On-Hit: 56/84/95 AP ⇒ 62/92/105 AP
* Kayle Wave Damage: 40/40/40/50 AP ⇒ 35/35/35/45 AP
* Shen Shield: 325/400/500/600 AP ⇒ 350/430/550/700 AP
* Warwick AD: 40 ⇒ 45
* Yunara Ability Damage: 150/225/335/570 AD ⇒ 160/240/370/630 AD
---
#### UNITS: TIER 3
> Azir and Mama Beak released on the weaker end after having a wild PBE arc. We’re buffing the two to summon a new potential reroll comp.  
>   
> Kha’Zix struggles to kill anything early game before getting items, often ending up just jumping around like a kid in a candy store: unfocused, overly excited, and without the adult money to acquire anything on their own. An AD buff should help him auto-down his enemies so he can finish them off with a cast or two.  
>   
> Despite nerfs in one of our 18.1 mid-patch updates, Yi is still strong in both forms.  
>   
> A base Attack Speed nerf for Rengar should hit his most consistent build (Rageblade, Titan’s Resolve), hurting his ability to cast and heal up, sustaining himself throughout the fight.
* Azir Soldier Ability Damage: 40/60/96/165 AP ⇒ 43/65/103/175 AP
* Diana Ability Damage Per Orb: 70/105/170 AP ⇒ 75/115/180 AP
* Diana Shield: 150/275/400 ⇒ 150/275/500
* Kha’Zix Base AD: 30 ⇒ 40
* Mama Beak Base AD: 50 ⇒ 55
* Mama Beak Ability Damage: 20/30/48 AD ⇒ 22/33/48 AD
* Master Yi AD Form: Base AD: 65 ⇒ 60
* Master Yi AP Form: Ability Damage: 140/210/335 AP ⇒ 125/190/285 AP
* Rengar Base AS: 0.8 ⇒ 0.75
---
#### UNITS: TIER 4
> Every now and then, Sentinel gets too excited about targeting his current target and fires a shockwave off the board…oops. Despite that, Sentinel is still the best tank in the game right now, so while we are correcting this bug, we're shipping a pretty heavy nerf alongside it.
* Ahri Ability Damage: 425/640 AP ⇒ 455/685 AP
* Ahri Ability damage fall off Per Hex: 20% ⇒ 21%
* Brambleback Base AD: 115 ⇒ 120
* Brambleback Armor Ignore Base: 10% ⇒ 15%
* Brambleback Leap Damage: 170/255 AD ⇒ 155/235 AD
* Ezreal Primary Ability Damage: 235/355 AD ⇒ 250/375 AD
* Sentinel Now targets the largest line of enemies. No longer required to include his current target
* Sentinel Ability Shield: 400/500 AP ⇒ 350/450 AP
* Nidalee AP Form: Nidalee Empowered Attack Damage: 285/425 AP ⇒ 300/450 AP
* Zyra Ability Damage: 37/55 AP ⇒ 35/53
---
#### UNITS: TIER 5
> Not only is accessing our Legendary Units easier this patch with more gold in the bank, but the Legendary Units are also getting better! Between our mid-patch update buffs in 18.1 and here we’re buffing almost every one of our 5-costs…almost.  
>   
> Even the most legendary of Archer’s can lose focus sometimes and target the wrong line of enemies. So, it only makes sense that we should cut ourselves some slack in our everyday lives when we lose focus, cause unlike Ashe, we can’t be patched to lock in more AND do more damage with our ability. As an aside, what’s your Ability?  
>   
> Starting with three Ivern hexes, two of which are frontline hexes, should make slotting in Ivern feel like an immediate improvement to your board. And you're also one hex closer to that ever-illusive God Willow.  
>   
> Kennen’s getting smarter with his cast, which alongside a buff to vertical Infernal, might encourage you to stop, drop, and reroll the trait.  
>   
> Taric currently sees play as an unitemized supportive unit. We’re buffing him so that he’ll be a lot better with HP and even AP itemization, but will be somewhat neutral of a change if you don’t itemize him.
* Ashe Bugfix: No longer can sometimes target the wrong line of enemies.
* Ashe Arrow Damage: 440/660 AD ⇒ 465/700 AD
* Ivern Starting Hexes: 2 ⇒ 3
* Ivern Shield: 165/300 AP ⇒ 185/350 AP
* Ivern Ability Damage: 140/210 AP ⇒ 155/235 AP
* Kennen is now better at targeting groups of enemies for his Firestorm
* Lux Ability Damage: 355/550 AP ⇒ 375/565 AP
* Maokai Mana: 40/100 ⇒ 30/90
* Taric Passive Shield: 175/350 + 10% max HP ⇒ 100/225 + 15% max HP
* Taric Active Heal: 200/300 AP ⇒ 250/375 AP
---
#### ITEMS
> Bloodthirster and Hand of Justice have been weaker melee items than Edge of Night for two sets now. We’re giving them both buffs to keep them competitive with Edge of Night.  
>   
> Additionally, we're adjusting Edge of Night to trigger later, so that Edge of Night, Bloodthirster, and Sterak’s Gauge all have different HP thresholds and won’t grief each other as much when combined. This opens up a pretty bad, but funny, survive at all costs melee-carry build of stacking all three of these. One final note, if you do the math on the Edge of Night change, it is a teeny-tiny buff of 1% max HP healing.
* Bloodthirster Trigger Health: 40% ⇒ 50%
* Bloodthirster AD/AP: 15% ⇒ 18%
* Bloodthirster Shield: 25% max HP ⇒ 30% max HP
* Edge of Night Trigger Health: 60% ⇒ 40%
* Edge of Night Missing Health Heal: 20% ⇒ 15%
* Hand of Justice Base AD/AP: 15% ⇒ 18%
* Hand of Justice Base Omnivamp: 12% ⇒ 15%
---
#### RADIANT ITEMS
> As above, so aglow below.
* Radiant Bloodthirster Trigger Health: 40% ⇒ 50%
* Radiant Bloodthirster AD/AP: 30% ⇒ 40%
* Radiant Bloodthirster Shield: 50% max HP ⇒ 60% max HP
* Radiant Edge of Night Trigger Health: 60% ⇒ 40%
* Radiant Hand of Justice Base Omnivamp: 24% ⇒ 30%
---
#### ARTIFACTS
> We have much better users for Artifacts this set so we’ve gotta make a few adjustments here.
* Blighting Jewel MR Reduction: 4 ⇒ 3
* Flickerblades AS Per Attack: 5% ⇒ 4%
* Forbidden Idol Health: 400 ⇒ 500
* Luden’s Tempest On-Kill Flat Damage: 100 ⇒ 130
* Silvermere Dawn AD: 125% ⇒ 150%
* Wit’s End On-Hit Damage: 30/55/75/95/115 (stage 2-5) ⇒ 25/45/65/85/100
---
#### EMBLEMS
> Emblems are pretty strong right now, except Primal Emblem.
* Brawler Emblem Health: 250 ⇒ 150
* Fae Emblem Health: 250 ⇒ 200
* Fae Emblem AD/AP: 15% ⇒ 10%
* Hunter Emblem Base AD: 30% ⇒ 25%
* Invoker Emblem AP Per Mana Spent: 10% ⇒ 8%
* Juggernaut Emblem Health: 350 ⇒ 250
* Primal Emblem Attack Speed: 25% ⇒ 35%
* Sprykin Emblem Rider Bonus Attack Speed: 30% ⇒ 20%
* Sprykin Emblem Base Resists: 20 ⇒ 15
* Sprykin Emblem Additional Rider Resists: 20 ⇒ 15
* Vanguard Emblem Armor/MR: 30 ⇒ 25
---
#### AUGMENTS
> We’ve got a focused balance pass on Augments for our first main patch with a few noteworthy callouts. A few of our Augments can now only be taken by one player in the lobby so as not to force griefing right out of the gates. Consuming Flora’s Emblem effectiveness is coming down significantly, a source of power that has propelled a few Champions into the S-tier. Dark Ritual is getting very large buffs to empower that Cass/Morgana duo-carry fantasy. Prismatic Destiny+ will still be worth the click—unless it is not worth the click—click to find out!
* Baron’s Lair Stats given: 5% ⇒ 4%
* Capital Gains II Starting gold: 2 ⇒ 3
* Cursed Crown no longer grants 4% Durability
* Consuming Flora Emblem Trait Effectiveness: 200% ⇒ 150%, now exclusive to 1 player per lobby
* Coven Acolyte now exclusive to 1 player per lobby together with Dark Ritual
* Dark Ritual now exclusive to 1 player per lobby together with Coven Acolyte
* Dark Ritual AP from cashouts:
  + Cashout 1: 5 ⇒ 7
  + Cashout 2:12 ⇒ 15
  + Cashout 3:40 ⇒ 50
  + Cashout 4:60 ⇒ 75
  + Cashout 5:100 ⇒ 125
  + Cashout 6: 175 ⇒ 200
  + Cashout 7: 250 ⇒ 300
* Dummify HP per round: 1000 ⇒ 1150
* Going Long XP is only granted after Player Combat
* Gold Destiny+ Gold: 6 ⇒ 5
* Golden Dragon Durability: 20% ⇒ 15%
* Hold The Line AP given: 9% ⇒ 10, AD given: 8% ⇒ 9
* Investment Strategy II HP given: 9 ⇒ 10
* Magic Roll: Fixed a bug where the champion reward gave less gold than intended
* Prismatic Destiny+ Gold: 10 ⇒ 7
* Shimmerscale Essence Delayed rounds: 7 ⇒ 8
* Spreading Roots now grants 1 emblem immediately and 1 after 3 rounds. Initial Gold removed.
* Spreading Roots+ no longer grants a reforger
* Trait Ladder now exclusive to 1 player, 10 trait cashout: 18 Gold, 11 trait cashout: Tactician item
* Trait Tree Plus and Cooking Pot are now mutually exclusive
* Unrivaled Mana gained from Kha’Zix to Rengar: 70% ⇒ 50%
* Unrivaled Healing from Rengar to Kha’Zix: 50% ⇒ 25%
---
#### WISPS
> The cost of Combat Wisps is coming down for just about all of them. Aside from that, we’re lowering the cost of a few other Wisps to save your gold so you can buy MORE WISPS, or Units, or XP…
* Combat Wisps:
  + Barrier Cost: 4g ⇒ 3g
  + Backrow Star Cost: 3g ⇒ 1g
  + Borrowed Gear Now gives item at the beginning of combat phase
  + "At the start of combat, a champion gains a temporary recommended item."
  + Bunch-o-Belts Cost: 2g ⇒ 1g
  + Combust Cost: 5g ⇒ 3g, Max Health Damage: 15% ⇒ 12%
  + Downpour Cost: 3g ⇒ 2g
  + Infliction Cost: 6g ⇒ 4g
  + Ironwood Cost: 3g ⇒ 2g
  + Late Bloomer Cost: 6g ⇒ 4g
  + Lightning Storm Cost: 5g ⇒ 3g
  + Lightning Strike Cost: 2g ⇒ 1g
  + Blaze Cost: 5g ⇒ 3g
  + Fellowship Gold: 4g ⇒ 3g
  + Giant’s Aura Cost: 5g ⇒ 3g
  + Hero’s Entrance Gold: 4g ⇒ 2g
  + Hireling Cost: 5g ⇒ 2g
  + Iron Core Cost: 2g ⇒ 1g
  + Killing Frenzy Cost: 3g ⇒ 2g
  + Killer’s Regret Cost: 2g ⇒ 1g
  + Mana-Rich Soil Cost: 3g ⇒ 2g
  + Petrify Shields Cost: 2g ⇒ 1g
  + Potted Stonebark Cost: 2g/1g ⇒ 1g/0g
  + Potted Lifebloom Cost: 2g/1g ⇒ 1g/0g
  + Phantom Emblem Cost: 3g ⇒ 2g
  + Radiantize Cost: 4g ⇒ 3g
  + Revenge Cost: 3g ⇒ 2g
  + Solitude’s Cloak Cost: 3g ⇒ 2g
  + Stand Alone Cost: 3g ⇒ 2g
  + Supercritical Cost: 3g ⇒ 2g
  + Treetop Archers Cost: 5g ⇒ 3g
  + Tremors Cost: 4g ⇒ 3g
  + Yordle Spirit Cost: 3g ⇒ 2g
* Economy Wisps:
  + Cutpurse: Cost: 3g ⇒ 2g, Gold Chance: 15% ⇒ 20%
  + Good Loss Cost: 5g ⇒ 4g
  + Payday Cost: 4g ⇒ 3g
  + Slow Study Cost: 4g ⇒ 2g
* Shop Wisps:
  + All Fives Cost: 10g ⇒ 8g
  + All Fours Cost: 4g ⇒ 3g
  + Border Village Cost: 6/4g ⇒ 3/2g
  + Field of Mice has been Removed
  + Flash Fire Cost: 2g ⇒ 1g
  + Middle Path Cost: 6/4g ⇒ 4/3g
  + Roly-Polys Cost: 4g ⇒ 3g
  + Search Party Cost: 3/1g ⇒ 1/0g
  + Starting Town Cost: 3/2g ⇒ 2/1g
* Other Wisps:
  + Potioncraft Cost: 3g ⇒ 2g
  + Smurfing Cost: 7g/6g ⇒ 6g/5g
## SMALL CHANGES
> Small, like a lifetime.
---
#### UNITS
* 3-star 4-costs:
  + Brambleback Armor Ignore: 10 + 50% AP ⇒ 10 + 70% AP
  + Brambleback Leap Damage: 600% AD ⇒ 1000% AD
  + Brambleback Bonus Ability AD: 280% ⇒ 300%
  + Nidalee AD Form Ability Damage: 2500% AD ⇒ 3000% AD
* 3-star 5-costs:
  + Gnar Rage Per Attack: 5 ⇒ 20
  + Gnar Resist Reduction: 100 ⇒ 250
  + Gnar Bonus Health: 10000 ⇒ 15000
  + Lux Laser Damage: 5000 AP ⇒ 6500 AP
## BUG FIXES
* MOBILE: Login persistence on Mobile has been restored after becoming temporarily disabled with our D-patch
* Early Learning’s 5% starting Attack Damage and Ability Power is now correctly doubled for 1-costs
* Fixed a bug where Augments intended to be offered to only one player could occasionally be offered to multiple players.
* Good for Something now correctly gives gold based on the percentage chance.
* Cooking Pot and Trait Tree are now properly excluded
* Elderwood Deepwood Protector’s knockup now properly respects Unstoppable
* Fixed a Yorick tooltip inconsistency referring to a ‘Ghoul’ rather than a Spirit Walker
* Coven Emblem is no longer offered on carousel after stage 5
* Draven’s Bounty Seeker trait will no longer offer quests to gain XP if you’re level 10.
* 2-star Units bought from the shop will have the correct 2-star highlighting and size.
* PvE loot will now not land on top of PvE opponents in most scenarios.
* Akali can no longer sometimes get more damage from Lich Bane procs than intended
* Krug’s Alpha Mark shield grants the proper Shield when Kruglettes die before the shield missile lands.
* Thief's Gloves on Ghost boards now match the Thief's Gloves rolls from the source board
* Murk Wolf now cannot leap to targets 4 hexes away in certain situations
* Double Trouble Re-enabled. Fixed Adaptors of different types failing to gain the effect. Fixed 2-star copies created occasionally double-counting their traits
* Edge of Night effect no longer persists after breaking apart the item with the Salvager wisp
* Hullcrusher health persists when units are summoned during combat. Re-enabled
* Kha’Zix’s Ability visuals are now correctly timed when he has the Unrivaled augment bonus active and hits an isolated unit
* Blossom empowered Essence Theft now properly displays its 1g gold cost
* Burn VFX from inferno units is now correctly visible
* VFX for melee units with extended range should now be visible in all scenarios and look much better
* Fixed instances where Yorick’s Spirit Walker persists on the Bench after starring up during Combat Phase
* Fixed instances where units display wrong colored health bars when scouting an opponent
* Tactician no longer disappears when right-clicking on the player's arena right before the carousel arrival phase
## COSMETICS CONVERTED IN PATCH 18.2
> 39 Cosmetics have been added with Patch 18.2.
---
* Legendary Arenas (10): High Noon Saloon, Frostguard Arena, Splash Party Arena, The Toxitorium, Winter's Claw Arena, Hextech Battle Arena, Count Spatula Arena, Avarosa Arena, Odyssey, Malphite Arena, Reckoner Arena
* Mythic Arenas (2): Mecha Prime Zero, Choncc's Splash Resort
* Mythic Chibi (5): Chibi Spirit Blossom Yone, Chibi Shork Cosplay Briar, Chibi Crystal Rose Gwen, Chibi Dragonmancer Lee Sin, Chibi Spirit Blossom Ahri
* Mythic Unbound (1): High Noon Thresh Unbound
* Prestige Boom (2): Prestige Dragon Fist Rage, Prestige Star Nemesis Soul Shackles
* Prestige Chibi (2): Prestige Chibi Spirit Blossom Ahri, Prestige Chibi Dawnbringer Yone
* Standard Arena (2): Verdant Arena, Biosphere Central
* Standard Boom (9): The Monster Inside, Hextech Hypersurge, Max Volume, Asteroid Pelt, Bandle Blast!, To Battle Stations!, Abyssal Chasm, Hextech Wipeout, Infernal Flock
* Little Legend (6): Galaxy Slayer Abyssia, Demacian Sprite, PROJECT: Abyssia, Hextech Fenroar, Honeybuzz Bungo, Bun Bun
## COSMETICS BEING CONVERTED NEXT PATCH (18.3)
> For Patch 18.3 we’re on track to add over 40 cosmetics from the judgemental Chibi Majestic Empress Morgana to the already judged Chibi Little Devil Teemo. There is a chance we’ll find an issue that results in a change to the final number we’re converting, but we’ll keep everyone informed on the final list when it’s locked in.
---
* Legendary Arena (10): Aurora Peak, Golden Bakery, Cyber City Streets, Bridge of Progress, Akana Arena, Kanmei Arena, Festival Arena, Magic Duel Arena, Enchanted Archives, Club 2 Arena
* Legendary Boom (4): Final Spark, Earn Your Legacy, Curse of the Sad Mummy, Bootcamp Boom
* Mythic Arena (6): Gwen's Snip Snip Spire, Peak URF, Everything Goes On, Le Bunny Bonbon Bistro, Graffiti Chic Street, Night Versus Dawn
* Mythic Boom (6): Spirit Blossom Orb of Deception, Needlework, Crystal Rose Snip Snip!, Dark Cosmic Curtain Call, Arcane Super Mega Death Rocket!, Star Guardian Perfect Execution
* Mythic Chibi (5): Chibi Soul Fighter Gwen, Chibi Majestic Empress Morgana, Chibi Divine Sword Irelia, Chibi Little Devil Teemo, Chibi Star Guardian Ahri
* Mythic Unbound (4): Arcane Jinx Unbound, God-King Garen Unbound, T1 Pyke Unbound, Pengaren Unbound
* Prestige Chibi (6): Prestige Chibi Dragon Fist Lee Sin, Chibi Cafe Cuties Gwen, Prestige Chibi Valiant Sword Riven, Chibi Headliner K/DA POP/STARS Kai'Sa, Chibi Prestige Arcane Superfan Annie, Prestige Chibi Porcelain Ezreal
* Base Chibi (12): Chibi Annie, Chibi Teemo, Chibi Caitlyn, Chibi Yuumi, Chibi Akali, Chibi Lulu, Chibi Lux, Chibi Kai'Sa, Chibi Miss Fortune, Chibi Jinx, Chibi Briar, Chibi Aatrox