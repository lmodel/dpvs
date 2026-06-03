---
search:
  boost: 10.0
---

# Class: BrowserHistory 


_Information about and including web browsing history_



<div data-search-exclude markdown="1">



URI: [pd:BrowserHistory](https://w3id.org/lmodel/dpv/pd/BrowserHistory)





```mermaid
 classDiagram
    class BrowserHistory
    click BrowserHistory href "../BrowserHistory/"
      BrowsingBehaviour <|-- BrowserHistory
        click BrowsingBehaviour href "../BrowsingBehaviour/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * [BrowsingBehaviour](BrowsingBehaviour.md)
            * **BrowserHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BrowserHistory](https://w3id.org/lmodel/dpv/pd/BrowserHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Browser History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BrowserHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BrowserHistory |
| native | pd:BrowserHistory |
| exact | dpv_pd:BrowserHistory, dpv_pd_owl:BrowserHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BrowserHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowserHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about and including web browsing history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browser History
exact_mappings:
- dpv_pd:BrowserHistory
- dpv_pd_owl:BrowserHistory
is_a: BrowsingBehaviour
class_uri: pd:BrowserHistory

```
</details>

### Induced

<details>
```yaml
name: BrowserHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowserHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about and including web browsing history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browser History
exact_mappings:
- dpv_pd:BrowserHistory
- dpv_pd_owl:BrowserHistory
is_a: BrowsingBehaviour
class_uri: pd:BrowserHistory

```
</details></div>