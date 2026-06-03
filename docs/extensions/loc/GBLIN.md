---
search:
  boost: 10.0
---

# Class: GBLIN 


_Concept representing region Lincolnshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LIN](https://w3id.org/lmodel/dpv/loc/GB-LIN)





```mermaid
 classDiagram
    class GBLIN
    click GBLIN href "../GBLIN/"
      GB <|-- GBLIN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLIN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LIN](https://w3id.org/lmodel/dpv/loc/GB-LIN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LIN
* Lincolnshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LIN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LIN |
| native | loc:GBLIN |
| exact | dpv_loc:GB-LIN, dpv_loc_owl:GB-LIN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LIN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lincolnshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LIN
- Lincolnshire
exact_mappings:
- dpv_loc:GB-LIN
- dpv_loc_owl:GB-LIN
is_a: GB
class_uri: loc:GB-LIN

```
</details>

### Induced

<details>
```yaml
name: GBLIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LIN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Lincolnshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LIN
- Lincolnshire
exact_mappings:
- dpv_loc:GB-LIN
- dpv_loc_owl:GB-LIN
is_a: GB
class_uri: loc:GB-LIN

```
</details></div>