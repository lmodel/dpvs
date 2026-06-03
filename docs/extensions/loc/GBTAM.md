---
search:
  boost: 10.0
---

# Class: GBTAM 


_Concept representing region Metropolitan Borough of Tameside in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-TAM](https://w3id.org/lmodel/dpv/loc/GB-TAM)





```mermaid
 classDiagram
    class GBTAM
    click GBTAM href "../GBTAM/"
      GB <|-- GBTAM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBTAM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-TAM](https://w3id.org/lmodel/dpv/loc/GB-TAM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-TAM
* Metropolitan Borough of Tameside




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-TAM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-TAM |
| native | loc:GBTAM |
| exact | dpv_loc:GB-TAM, dpv_loc_owl:GB-TAM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBTAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TAM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan Borough of Tameside in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TAM
- Metropolitan Borough of Tameside
exact_mappings:
- dpv_loc:GB-TAM
- dpv_loc_owl:GB-TAM
is_a: GB
class_uri: loc:GB-TAM

```
</details>

### Induced

<details>
```yaml
name: GBTAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TAM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan Borough of Tameside in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TAM
- Metropolitan Borough of Tameside
exact_mappings:
- dpv_loc:GB-TAM
- dpv_loc_owl:GB-TAM
is_a: GB
class_uri: loc:GB-TAM

```
</details></div>