---
search:
  boost: 10.0
---

# Class: ITBR 


_Concept representing region Province of Brindisi in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BR](https://w3id.org/lmodel/dpv/loc/IT-BR)





```mermaid
 classDiagram
    class ITBR
    click ITBR href "../ITBR/"
      IT <|-- ITBR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BR](https://w3id.org/lmodel/dpv/loc/IT-BR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BR
* Province of Brindisi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BR |
| native | loc:ITBR |
| exact | dpv_loc:IT-BR, dpv_loc_owl:IT-BR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Brindisi in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BR
- Province of Brindisi
exact_mappings:
- dpv_loc:IT-BR
- dpv_loc_owl:IT-BR
is_a: IT
class_uri: loc:IT-BR

```
</details>

### Induced

<details>
```yaml
name: ITBR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Brindisi in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BR
- Province of Brindisi
exact_mappings:
- dpv_loc:IT-BR
- dpv_loc_owl:IT-BR
is_a: IT
class_uri: loc:IT-BR

```
</details></div>