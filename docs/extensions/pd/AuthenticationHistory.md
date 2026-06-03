---
search:
  boost: 10.0
---

# Class: AuthenticationHistory 


_Information about prior authentication and its outcomes such as login_

_attempts or location_



<div data-search-exclude markdown="1">



URI: [pd:AuthenticationHistory](https://w3id.org/lmodel/dpv/pd/AuthenticationHistory)





```mermaid
 classDiagram
    class AuthenticationHistory
    click AuthenticationHistory href "../AuthenticationHistory/"
      Behavioural <|-- AuthenticationHistory
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **AuthenticationHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:AuthenticationHistory](https://w3id.org/lmodel/dpv/pd/AuthenticationHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Authentication History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#AuthenticationHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:AuthenticationHistory |
| native | pd:AuthenticationHistory |
| exact | dpv_pd:AuthenticationHistory, dpv_pd_owl:AuthenticationHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AuthenticationHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AuthenticationHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about prior authentication and its outcomes such as login

  attempts or location'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Authentication History
exact_mappings:
- dpv_pd:AuthenticationHistory
- dpv_pd_owl:AuthenticationHistory
is_a: Behavioural
class_uri: pd:AuthenticationHistory

```
</details>

### Induced

<details>
```yaml
name: AuthenticationHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AuthenticationHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about prior authentication and its outcomes such as login

  attempts or location'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Authentication History
exact_mappings:
- dpv_pd:AuthenticationHistory
- dpv_pd_owl:AuthenticationHistory
is_a: Behavioural
class_uri: pd:AuthenticationHistory

```
</details></div>