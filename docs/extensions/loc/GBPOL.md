---
search:
  boost: 10.0
---

# Class: GBPOL 


_Concept representing region Borough of Poole in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-POL](https://w3id.org/lmodel/dpv/loc/GB-POL)





```mermaid
 classDiagram
    class GBPOL
    click GBPOL href "../GBPOL/"
      GB <|-- GBPOL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBPOL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-POL](https://w3id.org/lmodel/dpv/loc/GB-POL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-POL
* Borough of Poole




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-POL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-POL |
| native | loc:GBPOL |
| exact | dpv_loc:GB-POL, dpv_loc_owl:GB-POL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBPOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Poole in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POL
- Borough of Poole
exact_mappings:
- dpv_loc:GB-POL
- dpv_loc_owl:GB-POL
is_a: GB
class_uri: loc:GB-POL

```
</details>

### Induced

<details>
```yaml
name: GBPOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Poole in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POL
- Borough of Poole
exact_mappings:
- dpv_loc:GB-POL
- dpv_loc_owl:GB-POL
is_a: GB
class_uri: loc:GB-POL

```
</details></div>