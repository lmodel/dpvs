---
search:
  boost: 10.0
---

# Class: IEM 


_Concept representing region Munster, Ireland in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-M](https://w3id.org/lmodel/dpv/loc/IE-M)





```mermaid
 classDiagram
    class IEM
    click IEM href "../IEM/"
      IE <|-- IEM
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-M](https://w3id.org/lmodel/dpv/loc/IE-M) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-M
* Munster, Ireland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-M |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-M |
| native | loc:IEM |
| exact | dpv_loc:IE-M, dpv_loc_owl:IE-M |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Munster, Ireland in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-M
- Munster, Ireland
exact_mappings:
- dpv_loc:IE-M
- dpv_loc_owl:IE-M
is_a: IE
class_uri: loc:IE-M

```
</details>

### Induced

<details>
```yaml
name: IEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Munster, Ireland in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-M
- Munster, Ireland
exact_mappings:
- dpv_loc:IE-M
- dpv_loc_owl:IE-M
is_a: IE
class_uri: loc:IE-M

```
</details></div>