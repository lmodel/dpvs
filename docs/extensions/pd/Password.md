---
search:
  boost: 10.0
---

# Class: Password 


_Information about password used in the process of authenticating the_

_individual as an user accessing a system._



<div data-search-exclude markdown="1">



URI: [pd:Password](https://w3id.org/lmodel/dpv/pd/Password)





```mermaid
 classDiagram
    class Password
    click Password href "../Password/"
      Authenticating <|-- Password
        click Authenticating href "../Authenticating/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Authenticating](Authenticating.md)
        * **Password**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Password](https://w3id.org/lmodel/dpv/pd/Password) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Password




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Password |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Password |
| native | pd:Password |
| exact | dpv_pd:Password, dpv_pd_owl:Password |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Password
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Password
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about password used in the process of authenticating the

  individual as an user accessing a system.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Password
exact_mappings:
- dpv_pd:Password
- dpv_pd_owl:Password
is_a: Authenticating
class_uri: pd:Password

```
</details>

### Induced

<details>
```yaml
name: Password
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Password
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about password used in the process of authenticating the

  individual as an user accessing a system.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Password
exact_mappings:
- dpv_pd:Password
- dpv_pd_owl:Password
is_a: Authenticating
class_uri: pd:Password

```
</details></div>