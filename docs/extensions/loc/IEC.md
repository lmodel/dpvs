---
search:
  boost: 10.0
---

# Class: IEC 


_Concept representing region Connacht in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-C](https://w3id.org/lmodel/dpv/loc/IE-C)





```mermaid
 classDiagram
    class IEC
    click IEC href "../IEC/"
      IE <|-- IEC
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-C](https://w3id.org/lmodel/dpv/loc/IE-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-C
* Connacht




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-C |
| native | loc:IEC |
| exact | dpv_loc:IE-C, dpv_loc_owl:IE-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Connacht in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-C
- Connacht
exact_mappings:
- dpv_loc:IE-C
- dpv_loc_owl:IE-C
is_a: IE
class_uri: loc:IE-C

```
</details>

### Induced

<details>
```yaml
name: IEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Connacht in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-C
- Connacht
exact_mappings:
- dpv_loc:IE-C
- dpv_loc_owl:IE-C
is_a: IE
class_uri: loc:IE-C

```
</details></div>