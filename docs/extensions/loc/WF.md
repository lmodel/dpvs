---
search:
  boost: 10.0
---

# Class: WF 


_Concept representing Country of Wallis and Futuna Islands_



<div data-search-exclude markdown="1">



URI: [loc:WF](https://w3id.org/lmodel/dpv/loc/WF)





```mermaid
 classDiagram
    class WF
    click WF href "../WF/"
      FR <|-- WF
        click FR href "../FR/"
      

      WF <|-- WFAL
        click WFAL href "../WFAL/"
      WF <|-- WFSG
        click WFSG href "../WFSG/"
      WF <|-- WFUV
        click WFUV href "../WFUV/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **WF**
            * [WFAL](WFAL.md)
            * [WFSG](WFSG.md)
            * [WFUV](WFUV.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:WF](https://w3id.org/lmodel/dpv/loc/WF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Wallis and Futuna Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#WF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:WF |
| native | loc:WF |
| exact | dpv_loc:WF, dpv_loc_owl:WF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#WF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Wallis and Futuna Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Wallis and Futuna Islands
exact_mappings:
- dpv_loc:WF
- dpv_loc_owl:WF
is_a: FR
class_uri: loc:WF

```
</details>

### Induced

<details>
```yaml
name: WF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#WF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Wallis and Futuna Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Wallis and Futuna Islands
exact_mappings:
- dpv_loc:WF
- dpv_loc_owl:WF
is_a: FR
class_uri: loc:WF

```
</details></div>