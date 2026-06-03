---
search:
  boost: 10.0
---

# Class: Residency 


_Information about residency e.g. which region or country a person is_

_resident in_



<div data-search-exclude markdown="1">



URI: [pd:Residency](https://w3id.org/lmodel/dpv/pd/Residency)





```mermaid
 classDiagram
    class Residency
    click Residency href "../Residency/"
      DpvLocation <|-- Residency
        click DpvLocation href "../DpvLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **Residency**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Residency](https://w3id.org/lmodel/dpv/pd/Residency) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Residency


## Comments

* Parent changed to pd:Location



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Residency |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Residency |
| native | pd:Residency |
| exact | dpv_pd:Residency, dpv_pd_owl:Residency |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Residency
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Residency
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about residency e.g. which region or country a person is

  resident in'
comments:
- Parent changed to pd:Location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Residency
exact_mappings:
- dpv_pd:Residency
- dpv_pd_owl:Residency
is_a: DpvLocation
class_uri: pd:Residency

```
</details>

### Induced

<details>
```yaml
name: Residency
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Residency
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about residency e.g. which region or country a person is

  resident in'
comments:
- Parent changed to pd:Location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Residency
exact_mappings:
- dpv_pd:Residency
- dpv_pd_owl:Residency
is_a: DpvLocation
class_uri: pd:Residency

```
</details></div>