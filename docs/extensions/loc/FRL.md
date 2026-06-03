---
search:
  boost: 10.0
---

# Class: FRL 


_Concept representing region Limousin in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-L](https://w3id.org/lmodel/dpv/loc/FR-L)





```mermaid
 classDiagram
    class FRL
    click FRL href "../FRL/"
      FR <|-- FRL
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-L](https://w3id.org/lmodel/dpv/loc/FR-L) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-L
* Limousin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-L |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-L |
| native | loc:FRL |
| exact | dpv_loc:FR-L, dpv_loc_owl:FR-L |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Limousin in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-L
- Limousin
exact_mappings:
- dpv_loc:FR-L
- dpv_loc_owl:FR-L
is_a: FR
class_uri: loc:FR-L

```
</details>

### Induced

<details>
```yaml
name: FRL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Limousin in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-L
- Limousin
exact_mappings:
- dpv_loc:FR-L
- dpv_loc_owl:FR-L
is_a: FR
class_uri: loc:FR-L

```
</details></div>