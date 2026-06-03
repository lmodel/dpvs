---
search:
  boost: 10.0
---

# Class: TravelHistory 


_Information about travel history_



<div data-search-exclude markdown="1">



URI: [pd:TravelHistory](https://w3id.org/lmodel/dpv/pd/TravelHistory)





```mermaid
 classDiagram
    class TravelHistory
    click TravelHistory href "../TravelHistory/"
      DpvLocation <|-- TravelHistory
        click DpvLocation href "../DpvLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **TravelHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:TravelHistory](https://w3id.org/lmodel/dpv/pd/TravelHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Travel History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#TravelHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:TravelHistory |
| native | pd:TravelHistory |
| exact | dpv_pd:TravelHistory, dpv_pd_owl:TravelHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TravelHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TravelHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about travel history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Travel History
exact_mappings:
- dpv_pd:TravelHistory
- dpv_pd_owl:TravelHistory
is_a: DpvLocation
class_uri: pd:TravelHistory

```
</details>

### Induced

<details>
```yaml
name: TravelHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TravelHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about travel history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Travel History
exact_mappings:
- dpv_pd:TravelHistory
- dpv_pd_owl:TravelHistory
is_a: DpvLocation
class_uri: pd:TravelHistory

```
</details></div>