---
search:
  boost: 10.0
---

# Class: GBEAL 


_Concept representing region London Borough of Ealing in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-EAL](https://w3id.org/lmodel/dpv/loc/GB-EAL)





```mermaid
 classDiagram
    class GBEAL
    click GBEAL href "../GBEAL/"
      GB <|-- GBEAL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBEAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-EAL](https://w3id.org/lmodel/dpv/loc/GB-EAL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-EAL
* London Borough of Ealing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-EAL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-EAL |
| native | loc:GBEAL |
| exact | dpv_loc:GB-EAL, dpv_loc_owl:GB-EAL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBEAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Ealing in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EAL
- London Borough of Ealing
exact_mappings:
- dpv_loc:GB-EAL
- dpv_loc_owl:GB-EAL
is_a: GB
class_uri: loc:GB-EAL

```
</details>

### Induced

<details>
```yaml
name: GBEAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Ealing in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EAL
- London Borough of Ealing
exact_mappings:
- dpv_loc:GB-EAL
- dpv_loc_owl:GB-EAL
is_a: GB
class_uri: loc:GB-EAL

```
</details></div>