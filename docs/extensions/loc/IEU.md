---
search:
  boost: 10.0
---

# Class: IEU 


_Concept representing region Ulster in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-U](https://w3id.org/lmodel/dpv/loc/IE-U)





```mermaid
 classDiagram
    class IEU
    click IEU href "../IEU/"
      IE <|-- IEU
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-U](https://w3id.org/lmodel/dpv/loc/IE-U) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-U
* Ulster




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-U |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-U |
| native | loc:IEU |
| exact | dpv_loc:IE-U, dpv_loc_owl:IE-U |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-U
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ulster in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-U
- Ulster
exact_mappings:
- dpv_loc:IE-U
- dpv_loc_owl:IE-U
is_a: IE
class_uri: loc:IE-U

```
</details>

### Induced

<details>
```yaml
name: IEU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-U
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ulster in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-U
- Ulster
exact_mappings:
- dpv_loc:IE-U
- dpv_loc_owl:IE-U
is_a: IE
class_uri: loc:IE-U

```
</details></div>