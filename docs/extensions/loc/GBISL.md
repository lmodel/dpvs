---
search:
  boost: 10.0
---

# Class: GBISL 


_Concept representing region London Borough of Islington in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ISL](https://w3id.org/lmodel/dpv/loc/GB-ISL)





```mermaid
 classDiagram
    class GBISL
    click GBISL href "../GBISL/"
      GB <|-- GBISL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBISL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ISL](https://w3id.org/lmodel/dpv/loc/GB-ISL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ISL
* London Borough of Islington




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ISL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ISL |
| native | loc:GBISL |
| exact | dpv_loc:GB-ISL, dpv_loc_owl:GB-ISL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBISL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ISL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Islington in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ISL
- London Borough of Islington
exact_mappings:
- dpv_loc:GB-ISL
- dpv_loc_owl:GB-ISL
is_a: GB
class_uri: loc:GB-ISL

```
</details>

### Induced

<details>
```yaml
name: GBISL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ISL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Islington in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ISL
- London Borough of Islington
exact_mappings:
- dpv_loc:GB-ISL
- dpv_loc_owl:GB-ISL
is_a: GB
class_uri: loc:GB-ISL

```
</details></div>