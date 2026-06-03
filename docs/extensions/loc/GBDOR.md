---
search:
  boost: 10.0
---

# Class: GBDOR 


_Concept representing region Dorset (district) in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DOR](https://w3id.org/lmodel/dpv/loc/GB-DOR)





```mermaid
 classDiagram
    class GBDOR
    click GBDOR href "../GBDOR/"
      GB <|-- GBDOR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DOR](https://w3id.org/lmodel/dpv/loc/GB-DOR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DOR
* Dorset (district)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DOR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DOR |
| native | loc:GBDOR |
| exact | dpv_loc:GB-DOR, dpv_loc_owl:GB-DOR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Dorset (district) in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DOR
- Dorset (district)
exact_mappings:
- dpv_loc:GB-DOR
- dpv_loc_owl:GB-DOR
is_a: GB
class_uri: loc:GB-DOR

```
</details>

### Induced

<details>
```yaml
name: GBDOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Dorset (district) in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DOR
- Dorset (district)
exact_mappings:
- dpv_loc:GB-DOR
- dpv_loc_owl:GB-DOR
is_a: GB
class_uri: loc:GB-DOR

```
</details></div>