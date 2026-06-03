---
search:
  boost: 10.0
---

# Class: HUVA 


_Concept representing region Vas County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-VA](https://w3id.org/lmodel/dpv/loc/HU-VA)





```mermaid
 classDiagram
    class HUVA
    click HUVA href "../HUVA/"
      HU <|-- HUVA
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUVA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-VA](https://w3id.org/lmodel/dpv/loc/HU-VA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-VA
* Vas County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-VA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-VA |
| native | loc:HUVA |
| exact | dpv_loc:HU-VA, dpv_loc_owl:HU-VA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vas County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VA
- Vas County
exact_mappings:
- dpv_loc:HU-VA
- dpv_loc_owl:HU-VA
is_a: HU
class_uri: loc:HU-VA

```
</details>

### Induced

<details>
```yaml
name: HUVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vas County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VA
- Vas County
exact_mappings:
- dpv_loc:HU-VA
- dpv_loc_owl:HU-VA
is_a: HU
class_uri: loc:HU-VA

```
</details></div>