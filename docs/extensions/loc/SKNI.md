---
search:
  boost: 10.0
---

# Class: SKNI 


_Concept representing region Nitra Region in country Slovakia_



<div data-search-exclude markdown="1">



URI: [loc:SK-NI](https://w3id.org/lmodel/dpv/loc/SK-NI)





```mermaid
 classDiagram
    class SKNI
    click SKNI href "../SKNI/"
      SK <|-- SKNI
        click SK href "../SK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SK](SK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SKNI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SK-NI](https://w3id.org/lmodel/dpv/loc/SK-NI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SK-NI
* Nitra Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SK-NI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SK-NI |
| native | loc:SKNI |
| exact | dpv_loc:SK-NI, dpv_loc_owl:SK-NI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SKNI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-NI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nitra Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-NI
- Nitra Region
exact_mappings:
- dpv_loc:SK-NI
- dpv_loc_owl:SK-NI
is_a: SK
class_uri: loc:SK-NI

```
</details>

### Induced

<details>
```yaml
name: SKNI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-NI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nitra Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-NI
- Nitra Region
exact_mappings:
- dpv_loc:SK-NI
- dpv_loc_owl:SK-NI
is_a: SK
class_uri: loc:SK-NI

```
</details></div>