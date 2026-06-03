---
search:
  boost: 10.0
---

# Class: BrowsingReferral 


_Information about web browsing referrer or referral, which can be based_

_on location, targeted referrals, direct, organic search, social media or_

_actions, campaigns._



<div data-search-exclude markdown="1">



URI: [pd:BrowsingReferral](https://w3id.org/lmodel/dpv/pd/BrowsingReferral)





```mermaid
 classDiagram
    class BrowsingReferral
    click BrowsingReferral href "../BrowsingReferral/"
      BrowsingBehaviour <|-- BrowsingReferral
        click BrowsingBehaviour href "../BrowsingBehaviour/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * [BrowsingBehaviour](BrowsingBehaviour.md)
            * **BrowsingReferral**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BrowsingReferral](https://w3id.org/lmodel/dpv/pd/BrowsingReferral) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Browsing Referral




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BrowsingReferral |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BrowsingReferral |
| native | pd:BrowsingReferral |
| exact | dpv_pd:BrowsingReferral, dpv_pd_owl:BrowsingReferral |
| related | iso29100:PIIProcessingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BrowsingReferral
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowsingReferral
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about web browsing referrer or referral, which can be based

  on location, targeted referrals, direct, organic search, social media or

  actions, campaigns.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browsing Referral
exact_mappings:
- dpv_pd:BrowsingReferral
- dpv_pd_owl:BrowsingReferral
related_mappings:
- iso29100:PIIProcessingActivity
is_a: BrowsingBehaviour
class_uri: pd:BrowsingReferral

```
</details>

### Induced

<details>
```yaml
name: BrowsingReferral
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowsingReferral
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about web browsing referrer or referral, which can be based

  on location, targeted referrals, direct, organic search, social media or

  actions, campaigns.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browsing Referral
exact_mappings:
- dpv_pd:BrowsingReferral
- dpv_pd_owl:BrowsingReferral
related_mappings:
- iso29100:PIIProcessingActivity
is_a: BrowsingBehaviour
class_uri: pd:BrowsingReferral

```
</details></div>