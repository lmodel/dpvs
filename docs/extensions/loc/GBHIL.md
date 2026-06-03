---
search:
  boost: 10.0
---

# Class: GBHIL 


_Concept representing region London Borough of Hillingdon in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-HIL](https://w3id.org/lmodel/dpv/loc/GB-HIL)





```mermaid
 classDiagram
    class GBHIL
    click GBHIL href "../GBHIL/"
      GB <|-- GBHIL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBHIL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-HIL](https://w3id.org/lmodel/dpv/loc/GB-HIL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-HIL
* London Borough of Hillingdon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-HIL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-HIL |
| native | loc:GBHIL |
| exact | dpv_loc:GB-HIL, dpv_loc_owl:GB-HIL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBHIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HIL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Hillingdon in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HIL
- London Borough of Hillingdon
exact_mappings:
- dpv_loc:GB-HIL
- dpv_loc_owl:GB-HIL
is_a: GB
class_uri: loc:GB-HIL

```
</details>

### Induced

<details>
```yaml
name: GBHIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HIL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Hillingdon in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HIL
- London Borough of Hillingdon
exact_mappings:
- dpv_loc:GB-HIL
- dpv_loc_owl:GB-HIL
is_a: GB
class_uri: loc:GB-HIL

```
</details></div>