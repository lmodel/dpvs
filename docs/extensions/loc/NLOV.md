---
search:
  boost: 10.0
---

# Class: NLOV 


_Concept representing region Overijssel in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-OV](https://w3id.org/lmodel/dpv/loc/NL-OV)





```mermaid
 classDiagram
    class NLOV
    click NLOV href "../NLOV/"
      NL <|-- NLOV
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLOV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-OV](https://w3id.org/lmodel/dpv/loc/NL-OV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-OV
* Overijssel




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-OV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-OV |
| native | loc:NLOV |
| exact | dpv_loc:NL-OV, dpv_loc_owl:NL-OV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-OV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Overijssel in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-OV
- Overijssel
exact_mappings:
- dpv_loc:NL-OV
- dpv_loc_owl:NL-OV
is_a: NL
class_uri: loc:NL-OV

```
</details>

### Induced

<details>
```yaml
name: NLOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-OV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Overijssel in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-OV
- Overijssel
exact_mappings:
- dpv_loc:NL-OV
- dpv_loc_owl:NL-OV
is_a: NL
class_uri: loc:NL-OV

```
</details></div>