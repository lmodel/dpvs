---
search:
  boost: 10.0
---

# Class: DpvCountry 


_Information about country e.g. residence, travel_



<div data-search-exclude markdown="1">



URI: [pd:Country](https://w3id.org/lmodel/dpv/pd/Country)





```mermaid
 classDiagram
    class DpvCountry
    click DpvCountry href "../DpvCountry/"
      DpvLocation <|-- DpvCountry
        click DpvLocation href "../DpvLocation/"
      

      DpvCountry <|-- BirthCountry
        click BirthCountry href "../BirthCountry/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **DpvCountry**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Country](https://w3id.org/lmodel/dpv/pd/Country) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Country




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Country |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Country |
| native | pd:DpvCountry |
| exact | dpv_pd:Country, dpv_pd_owl:Country |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvCountry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Country
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about country e.g. residence, travel
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Country
exact_mappings:
- dpv_pd:Country
- dpv_pd_owl:Country
is_a: DpvLocation
class_uri: pd:Country

```
</details>

### Induced

<details>
```yaml
name: DpvCountry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Country
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about country e.g. residence, travel
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Country
exact_mappings:
- dpv_pd:Country
- dpv_pd_owl:Country
is_a: DpvLocation
class_uri: pd:Country

```
</details></div>