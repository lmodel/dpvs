---
search:
  boost: 10.0
---

# Class: IEL 


_Concept representing region Leinster in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-L](https://w3id.org/lmodel/dpv/loc/IE-L)





```mermaid
 classDiagram
    class IEL
    click IEL href "../IEL/"
      IE <|-- IEL
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-L](https://w3id.org/lmodel/dpv/loc/IE-L) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-L
* Leinster




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-L |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-L |
| native | loc:IEL |
| exact | dpv_loc:IE-L, dpv_loc_owl:IE-L |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Leinster in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-L
- Leinster
exact_mappings:
- dpv_loc:IE-L
- dpv_loc_owl:IE-L
is_a: IE
class_uri: loc:IE-L

```
</details>

### Induced

<details>
```yaml
name: IEL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Leinster in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-L
- Leinster
exact_mappings:
- dpv_loc:IE-L
- dpv_loc_owl:IE-L
is_a: IE
class_uri: loc:IE-L

```
</details></div>