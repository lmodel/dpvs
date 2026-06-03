---
search:
  boost: 10.0
---

# Class: Historical 


_Information about historical data related to or relevant regarding_

_history or past events_



<div data-search-exclude markdown="1">



URI: [pd:Historical](https://w3id.org/lmodel/dpv/pd/Historical)





```mermaid
 classDiagram
    class Historical
    click Historical href "../Historical/"
      Historical <|-- LifeHistory
        click LifeHistory href "../LifeHistory/"
      
      
```





## Inheritance
* **Historical**
    * [LifeHistory](LifeHistory.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Historical](https://w3id.org/lmodel/dpv/pd/Historical) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Historical




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Historical |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Historical |
| native | pd:Historical |
| exact | dpv_pd:Historical, dpv_pd_owl:Historical |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Historical
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Historical
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about historical data related to or relevant regarding

  history or past events'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Historical
exact_mappings:
- dpv_pd:Historical
- dpv_pd_owl:Historical
class_uri: pd:Historical

```
</details>

### Induced

<details>
```yaml
name: Historical
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Historical
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about historical data related to or relevant regarding

  history or past events'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Historical
exact_mappings:
- dpv_pd:Historical
- dpv_pd_owl:Historical
class_uri: pd:Historical

```
</details></div>