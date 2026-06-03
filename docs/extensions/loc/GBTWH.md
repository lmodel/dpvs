---
search:
  boost: 10.0
---

# Class: GBTWH 


_Concept representing region London Borough of Tower Hamlets in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-TWH](https://w3id.org/lmodel/dpv/loc/GB-TWH)





```mermaid
 classDiagram
    class GBTWH
    click GBTWH href "../GBTWH/"
      GB <|-- GBTWH
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBTWH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-TWH](https://w3id.org/lmodel/dpv/loc/GB-TWH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-TWH
* London Borough of Tower Hamlets




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-TWH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-TWH |
| native | loc:GBTWH |
| exact | dpv_loc:GB-TWH, dpv_loc_owl:GB-TWH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBTWH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TWH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Tower Hamlets in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TWH
- London Borough of Tower Hamlets
exact_mappings:
- dpv_loc:GB-TWH
- dpv_loc_owl:GB-TWH
is_a: GB
class_uri: loc:GB-TWH

```
</details>

### Induced

<details>
```yaml
name: GBTWH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TWH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Tower Hamlets in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TWH
- London Borough of Tower Hamlets
exact_mappings:
- dpv_loc:GB-TWH
- dpv_loc_owl:GB-TWH
is_a: GB
class_uri: loc:GB-TWH

```
</details></div>