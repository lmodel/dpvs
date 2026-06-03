---
search:
  boost: 10.0
---

# Class: BrowsingBehaviour 


_Information about browsing behaviour_



<div data-search-exclude markdown="1">



URI: [pd:BrowsingBehaviour](https://w3id.org/lmodel/dpv/pd/BrowsingBehaviour)





```mermaid
 classDiagram
    class BrowsingBehaviour
    click BrowsingBehaviour href "../BrowsingBehaviour/"
      Behavioural <|-- BrowsingBehaviour
        click Behavioural href "../Behavioural/"
      

      BrowsingBehaviour <|-- BrowserHistory
        click BrowserHistory href "../BrowserHistory/"
      BrowsingBehaviour <|-- BrowsingReferral
        click BrowsingReferral href "../BrowsingReferral/"
      

      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **BrowsingBehaviour**
            * [BrowserHistory](BrowserHistory.md)
            * [BrowsingReferral](BrowsingReferral.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BrowsingBehaviour](https://w3id.org/lmodel/dpv/pd/BrowsingBehaviour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Browsing Behaviour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BrowsingBehaviour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BrowsingBehaviour |
| native | pd:BrowsingBehaviour |
| exact | dpv_pd:BrowsingBehaviour, dpv_pd_owl:BrowsingBehaviour |
| related | svd:OnlineActivity, iso29100:PIIProcessingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BrowsingBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowsingBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about browsing behaviour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browsing Behaviour
exact_mappings:
- dpv_pd:BrowsingBehaviour
- dpv_pd_owl:BrowsingBehaviour
related_mappings:
- svd:OnlineActivity
- iso29100:PIIProcessingActivity
is_a: Behavioural
class_uri: pd:BrowsingBehaviour

```
</details>

### Induced

<details>
```yaml
name: BrowsingBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowsingBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about browsing behaviour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browsing Behaviour
exact_mappings:
- dpv_pd:BrowsingBehaviour
- dpv_pd_owl:BrowsingBehaviour
related_mappings:
- svd:OnlineActivity
- iso29100:PIIProcessingActivity
is_a: Behavioural
class_uri: pd:BrowsingBehaviour

```
</details></div>