---
search:
  boost: 10.0
---

# Class: HUER 


_Concept representing region Érd in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-ER](https://w3id.org/lmodel/dpv/loc/HU-ER)





```mermaid
 classDiagram
    class HUER
    click HUER href "../HUER/"
      HU <|-- HUER
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUER**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-ER](https://w3id.org/lmodel/dpv/loc/HU-ER) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-ER
* Érd




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-ER |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-ER |
| native | loc:HUER |
| exact | dpv_loc:HU-ER, dpv_loc_owl:HU-ER |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Érd in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-ER
- Érd
exact_mappings:
- dpv_loc:HU-ER
- dpv_loc_owl:HU-ER
is_a: HU
class_uri: loc:HU-ER

```
</details>

### Induced

<details>
```yaml
name: HUER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Érd in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-ER
- Érd
exact_mappings:
- dpv_loc:HU-ER
- dpv_loc_owl:HU-ER
is_a: HU
class_uri: loc:HU-ER

```
</details></div>