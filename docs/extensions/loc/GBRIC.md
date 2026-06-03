---
search:
  boost: 10.0
---

# Class: GBRIC 


_Concept representing region London Borough of Richmond upon Thames in_

_country United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-RIC](https://w3id.org/lmodel/dpv/loc/GB-RIC)





```mermaid
 classDiagram
    class GBRIC
    click GBRIC href "../GBRIC/"
      GB <|-- GBRIC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBRIC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-RIC](https://w3id.org/lmodel/dpv/loc/GB-RIC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-RIC
* London Borough of Richmond upon Thames




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-RIC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-RIC |
| native | loc:GBRIC |
| exact | dpv_loc:GB-RIC, dpv_loc_owl:GB-RIC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBRIC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RIC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Richmond upon Thames in

  country United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RIC
- London Borough of Richmond upon Thames
exact_mappings:
- dpv_loc:GB-RIC
- dpv_loc_owl:GB-RIC
is_a: GB
class_uri: loc:GB-RIC

```
</details>

### Induced

<details>
```yaml
name: GBRIC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RIC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Richmond upon Thames in

  country United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RIC
- London Borough of Richmond upon Thames
exact_mappings:
- dpv_loc:GB-RIC
- dpv_loc_owl:GB-RIC
is_a: GB
class_uri: loc:GB-RIC

```
</details></div>